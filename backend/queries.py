from db import get_connection
from datetime import date

# USER

def create_user(name, email, daily_goal):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO "User" (name, email, daily_goal)
        VALUES (%s, %s, %s)
    """, (name, email, daily_goal))

    conn.commit()
    cur.close()
    conn.close()
    print("User created successfully")


def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM "User"
        WHERE user_id = %s
    """, (user_id,))

    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


def get_all_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT * FROM "User" """)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


# WATER LOG

def add_water_log(user_id, amount_water, met_goal, timestamp=date.today()):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO dailyWaterLog (user_id, amount_water, met_goal, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (user_id, amount_water, met_goal, timestamp))

    conn.commit()
    cur.close()
    conn.close()
    print("Water log added")


def get_user_logs(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM dailyWaterLog
        WHERE user_id = %s
        ORDER BY timestamp DESC
    """, (user_id,))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


# HISTORY / STREAKS

def get_history(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM History
        WHERE user_id = %s
    """, (user_id,))

    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


def update_history(user_id, streak, total_water):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE History
        SET streak = %s,
            total_water = %s
        WHERE user_id = %s
    """, (streak, total_water, user_id))

    conn.commit()
    cur.close()
    conn.close()


# COMMUNITY

def create_community(user_id, name, type_):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Community (user_id, name, type)
        VALUES (%s, %s, %s)
    """, (user_id, name, type_))

    conn.commit()
    cur.close()
    conn.close()
    print("Community created")


def join_community(user_id, community_id, community_date=date.today()):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO CommunityMember (user_id, community_id, community_date)
        VALUES (%s, %s, %s)
    """, (user_id, community_id, community_date))

    conn.commit()
    cur.close()
    conn.close()
    print("Joined community")


def get_user_communities(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.*
        FROM Community c
        JOIN CommunityMember cm ON c.community_id = cm.community_id
        WHERE cm.user_id = %s
    """, (user_id,))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def get_community_members(community_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT u.*
        FROM "User" u
        JOIN CommunityMember cm ON u.user_id = cm.user_id
        WHERE cm.community_id = %s
    """, (community_id,))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


# LEADERBOARD

def get_leaderboard(community_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Leaderboard
        WHERE community_id = %s
    """, (community_id,))

    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


# FRIENDS

def add_friend(user_id, friend_date=date.today()):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Friends (user_id, friend_date)
        VALUES (%s, %s)
    """, (user_id, friend_date))

    conn.commit()
    cur.close()
    conn.close()
    print("Friend added")


def get_friends(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Friends
        WHERE user_id = %s
    """, (user_id,))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


# -----------------------------
# NOTIFICATIONS
# -----------------------------

def send_notification(user_id, content, who_from):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Notification (user_id, content, who_from)
        VALUES (%s, %s, %s)
    """, (user_id, content, who_from))

    conn.commit()
    cur.close()
    conn.close()


def get_notifications(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM Notification
        WHERE user_id = %s
    """, (user_id,))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results