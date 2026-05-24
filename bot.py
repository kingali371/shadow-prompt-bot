# أوامر إضافية في bot.py

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """إحصائيات البوت"""
    user_id = str(update.effective_user.id)
    user = db_manager.get_user(user_id)
    
    # عدد المستخدمين الكلي
    with db_manager.get_connection() as conn:
        total_users = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
        total_prompts = conn.execute('SELECT COUNT(*) FROM prompts').fetchone()[0]
        
        # عدد برومبتات المستخدم
        user_prompts = conn.execute(
            'SELECT COUNT(*) FROM prompts WHERE user_id = ?',
            (user_id,)
        ).fetchone()[0]
    
    stats_text = f"""
📊 **إحصائيات البوت**

👥 إجمالي المستخدمين: {total_users}
📝 إجمالي البرومبتات: {total_prompts}
🎯 برومبتاتك الشخصية: {user_prompts}

✨ استمر في استخدام البوت!
"""
    await update.message.reply_text(stats_text, parse_mode='Markdown')

async def export_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تصدير برومبتات المستخدم"""
    user_id = str(update.effective_user.id)
    prompts = db_manager.get_user_prompts(user_id, limit=50)
    
    if not prompts:
        await update.message.reply_text("❌ لا توجد برومبتات للتصدير")
        return
    
    # إنشاء ملف نصي
    export_text = "# Shadow Prompt Bot - My Prompts\n\n"
    for prompt_text, ptype, date in prompts:
        export_text += f"## [{ptype}] - {date}\n{prompt_text}\n\n---\n\n"
    
    # إرسال الملف
    with open(f"export_{user_id}.txt", "w", encoding="utf-8") as f:
        f.write(export_text)
    
    await update.message.reply_document(
        document=open(f"export_{user_id}.txt", "rb"),
        filename=f"prompts_export_{datetime.now().strftime('%Y%m%d')}.txt"
    )
    
    # حذف الملف المحلي
    os.remove(f"export_{user_id}.txt")

async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """إرسال رسالة لجميع المستخدمين (للمالك فقط)"""
    user_id = str(update.effective_user.id)
    
    # تحقق من أن المستخدم هو المالك
    OWNER_ID = os.getenv("OWNER_ID", "123456789")  # ضع معرفك هنا
    
    if user_id != OWNER_ID:
        await update.message.reply_text("⛔ هذا الأمر للمالك فقط!")
        return
    
    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("⚠️ الرجاء كتابة الرسالة: /broadcast نص الرسالة")
        return
    
    # جلب جميع المستخدمين
    with db_manager.get_connection() as conn:
        users = conn.execute('SELECT user_id FROM users').fetchall()
    
    sent = 0
    failed = 0
    
    for user in users:
        try:
            await context.bot.send_message(
                chat_id=user[0],
                text=f"📢 **إعلان من المالك:**\n\n{message}",
                parse_mode='Markdown'
            )
            sent += 1
        except:
            failed += 1
        
        # تجنب الحظر
        await asyncio.sleep(0.1)
    
    await update.message.reply_text(f"✅ تم الإرسال\n📨 تم: {sent}\n❌ فشل: {failed}")
