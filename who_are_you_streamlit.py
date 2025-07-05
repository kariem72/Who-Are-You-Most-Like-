import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

st.set_page_config(page_title="Who Are You Most Like?", layout="centered")

@st.cache_data
def load_data():
    df = pd.read_csv('unique_1000_characters_dataset.csv', sep='\t')
    df.rename(columns={df.columns[0]: 'Character'}, inplace=True)
    df['Character'] = df['Character'].apply(lambda x: re.sub(r'\s*#\d+', '', x))
    trait_columns = ['BAP1', 'BAP2', 'BAP3', 'BAP4', 'BAP5']
    df = df[['Character'] + trait_columns]
    for col in trait_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    def get_category(name):
        name = name.lower()
        if 'cartoon' in name:
            return 'Cartoon'
        else:
            return 'Modern'
    df['Category'] = df['Character'].apply(get_category)
    df = df[df['Category'].isin(['Cartoon', 'Modern'])]
    df.set_index('Character', inplace=True)
    return df, trait_columns

df, trait_columns = load_data()

questions = {
    'BAP1': {
        "إيه أكتر حاجة بتحب تعملها؟": {
            "حل مسائل أو تفكير منطقي": 90,
            "ألعاب بسيطة أو حاجات مسلية": 40,
            "القراءة أو البرمجة أو التحليل": 80,
            "مش بفضل التفكير الكتير": 20
        }
    },
    'BAP2': {
        "بتتصرف إزاي وقت الضغط؟": {
            "بهدا وأحاول أركز": 90,
            "ببان هادي لكن ببقى مشدود": 70,
            "بتوتر بسرعة": 40,
            "بانفعل على طول": 20
        }
    },
    'BAP3': {
        "لما حد يستفزك، بتعمل إيه؟": {
            "بزعق فورًا": 90,
            "بتعصب جوايا": 70,
            "بمشي ومردش": 30,
            "بسكت ومش بعلق": 40
        }
    },
    'BAP4': {
        "لما حد يظلمك، رد فعلك؟": {
            "بواجهه بصراحة": 90,
            "بطنش": 30,
            "بطلب حد يساعدني": 60,
            "بستنى وقت مناسب وأتحرك": 70
        }
    },
    'BAP5': {
        "بتتعامل إزاي وسط صحابك؟": {
            "بهزر وأضحّكهم": 90,
            "ساكت وبضحك قليل": 50,
            "جدي في معظم الوقت": 30,
            "على حسب المود": 60
        }
    }
}

trait_names = {
    'BAP1': 'الذكاء / التحليل',
    'BAP2': 'الهدوء / التحكم',
    'BAP3': 'العصبية / الانفعال',
    'BAP4': 'الجرأة / الشجاعة',
    'BAP5': 'المرح / الاجتماعيّة'
}

def find_top_characters(user_scores, top_n=3):
    user_vector = np.array([user_scores[f'BAP{i+1}'] for i in range(5)]).reshape(1, -1)
    char_vectors = df[trait_columns].values
    similarities = cosine_similarity(user_vector, char_vectors)[0]
    df['Similarity'] = similarities
    top_cartoon = df[df['Category'] == 'Cartoon'].nlargest(top_n, 'Similarity')
    top_modern = df[df['Category'] == 'Modern'].nlargest(top_n, 'Similarity')
    return top_cartoon, top_modern

st.title("Who Are You Most Like?")
st.write("جاوب على شوية أسئلة بسيطة، وهقولك أنت شبه مين من الشخصيات الكرتونية والمشهورة")

user_scores = {}

with st.form("quiz_form"):
    for bap, qdata in questions.items():
        q_text = list(qdata.keys())[0]
        options = list(qdata[q_text].keys())
        answer = st.radio(f"{q_text}", options, key=bap)
        user_scores[bap] = qdata[q_text][answer]
    submitted = st.form_submit_button("اعرف شبيهي")

if submitted:
    top_cartoon, top_modern = find_top_characters(user_scores)

    st.subheader("النتيجة:")
    def show_list(title, df_list):
        st.markdown(f"**{title}:**")
        if df_list.empty:
            st.write("لا يوجد شخصيات مطابقة حالياً.")
        else:
            for i, (name, row) in enumerate(df_list.iterrows(), 1):
                st.write(f"{i}. {name} بنسبة شبه {row['Similarity']*100:.1f}%")

    show_list("الشخصيات الكرتونية الأقرب ليك", top_cartoon)
    show_list("الشخصيات المشهورة الأقرب ليك", top_modern)

    st.subheader("تحليل سماتك:")
    for i in range(5):
        dim = f'BAP{i+1}'
        st.write(f"{trait_names[dim]} → إنت: {user_scores[dim]}")
