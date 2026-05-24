from flask import Flask, render_template, jsonify, request
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('shadow_bot.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template('dashboard.html')

@app.route('/api/stats')
def get_stats():
    """إحصائيات البوت"""
    conn = get_db_connection()
    
    # عدد المستخدمين
    users_count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    
    # عدد البرومبتات
    prompts_count = conn.execute('SELECT COUNT(*) FROM prompts').fetchone()[0]
    
    # أكثر البرومبتات استخداماً
    top_prompts = conn.execute('''
        SELECT prompt_type, COUNT(*) as count 
        FROM prompts 
        GROUP BY prompt_type 
        ORDER BY count DESC
    ''').fetchall()
    
    # آخر 10 مستخدمين
    recent_users = conn.execute('''
        SELECT user_id, username, first_name, created_at 
        FROM users 
        ORDER BY created_at DESC 
        LIMIT 10
    ''').fetchall()
    
    conn.close()
    
    return jsonify({
        'users_count': users_count,
        'prompts_count': prompts_count,
        'top_prompts': [dict(row) for row in top_prompts],
        'recent_users': [dict(row) for row in recent_users]
    })

@app.route('/api/users')
def get_users():
    """قائمة المستخدمين"""
    conn = get_db_connection()
    users = conn.execute('''
        SELECT user_id, username, first_name, language, created_at, last_active 
        FROM users 
        ORDER BY last_active DESC
    ''').fetchall()
    conn.close()
    
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
