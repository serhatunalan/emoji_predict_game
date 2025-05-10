# -*- coding: utf-8 -*-
"""
Created on Sat May 10 22:55:57 2025

@author: SERHAT
"""

import streamlit as st
import random

# -----------------------------
# Emoji Veritabanı
# -----------------------------
emoji_questions = {
    "Film": [
        {"emoji": "🧑⚖️👨‍⚖️", "answer": "The Judge", "options": ["The Judge", "Lawyer Up", "Justice League", "Court Case"]},
        {"emoji": "🧑🦇🌃", "answer": "Batman", "options": ["Superman", "Batman", "Ironman", "Joker"]},
    ],
    "Yemek": [
        {"emoji": "🍕🍟", "answer": "Fast Food", "options": ["Salad", "Brunch", "Fast Food", "Bakery"]},
        {"emoji": "🍣🍱", "answer": "Sushi", "options": ["Sushi", "Ramen", "Taco", "Kebab"]},
    ],
    "Ülke": [
        {"emoji": "🗼🥖🇫🇷", "answer": "Fransa", "options": ["Fransa", "İtalya", "İspanya", "Belçika"]},
        {"emoji": "🗻🍣🇯🇵", "answer": "Japonya", "options": ["Çin", "Japonya", "Kore", "Tayland"]},
    ],
    "Şehir": [
        {"emoji": "🗽🚖🌆", "answer": "New York", "options": ["New York", "Londra", "Los Angeles", "Toronto"]},
        {"emoji": "🕌🌉🇹🇷", "answer": "İstanbul", "options": ["İstanbul", "Ankara", "Bursa", "İzmir"]},
    ]
}

# -----------------------------
# Oturum Başlatma
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.category = None
    st.session_state.questions = []

# -----------------------------
# Kategori Seçimi
# -----------------------------
st.title("🎉 Emoji Tahmin Oyunu")

if st.session_state.category is None:
    st.subheader("Bir kategori seçin:")
    category = st.radio("Kategori:", ["Film", "Yemek", "Ülke", "Şehir", "Karışık"])
    if st.button("Başla"):
        if category == "Karışık":
            all_questions = sum(emoji_questions.values(), [])
            random.shuffle(all_questions)
            st.session_state.questions = all_questions
        else:
            st.session_state.questions = emoji_questions[category].copy()
            random.shuffle(st.session_state.questions)
        st.session_state.category = category
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.experimental_rerun()

# -----------------------------
# Soru Gösterme
# -----------------------------
else:
    questions = st.session_state.questions
    index = st.session_state.question_index

    if index < len(questions):
        question = questions[index]
        st.markdown(f"### {question['emoji']}")
        answer = st.radio("Cevabınız:", question["options"], key=index)

        if st.button("Onayla", key=f"btn_{index}"):
            if answer == question["answer"]:
                st.success("Doğru! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Yanlış. Doğru cevap: {question['answer']}")
            st.session_state.question_index += 1
            st.experimental_rerun()
    else:
        st.subheader("🎯 Oyun Bitti!")
        st.success(f"Toplam Skor: {st.session_state.score} / {len(questions)}")
        if st.button("Yeniden Oyna"):
            st.session_state.category = None
            st.experimental_rerun()
