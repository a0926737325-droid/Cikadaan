import streamlit as st
import random
from datetime import datetime, date
import pandas as pd

# ==========================================
# 1. 系統設定
# ==========================================
st.set_page_config(
    page_title="南溪部落深度導覽 (長濱鄉三間村)",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (iPhone 深色模式/黑底黑字 修復專區)
# ==========================================
st.markdown("""
    <style>
    /* 1. 強制全站背景為淺大地/海洋色調，字體為深色 */
    .stApp {
        background-color: #F4F8F4; /* 替換原本的櫻粉色為淺森綠色，符合部落自然風 */
        font-family: "Microsoft JhengHei", sans-serif;
        color: #333333 !important;
    }
    
    /* 2. 強制所有一般文字元素為深色 */
    p, div, span, h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #333333 !important;
    }

    /* === 3. 核心修復：強制輸入框與選單在深色模式下維持「白底黑字」 === */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="base-input"] > input,
    .stTextInput input, 
    .stNumberInput input,
    .stDateInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important; 
    }
    div[data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }
    div[role="listbox"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }
    div[role="listbox"] li:hover {
        background-color: #E8F5E9 !important; /* 懸浮色改為淺綠 */
    }

    /* === 4. 客製化卡片 UI === */
    .spot-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border-left: 5px solid #4CAF50; /* 綠色邊框代表山林 */
        color: #333333;
    }
    .route-card {
        background: #E8F5E9; /* 淺綠底色 */
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px dashed #A5D6A7;
        color: #1B5E20;
    }
    .hotel-card {
        background: white;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 5px solid #FF9800; /* 橘色邊框代表住宿溫
