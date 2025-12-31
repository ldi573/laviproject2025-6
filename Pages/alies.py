import os #Operating System - פונה למערכת ההפעלה של המחשב
from dotenv import load_dotenv  #הספריה שהורדנו - של משתני הסביבה
from google import genai #generative ai = בינה מלאכותית יוצרת
import streamlit as st #ספריה של ממשקים GUI

st.set_page_config(
    Page_title="משחק אליאס מול AI",
    Page_icon='🤖'
)

st.title("משחק אליאס ")

load_dotenv() #טוענים את המשתנים
API_KEY = os.getenv("API_KEY") #פונים לקובץ env - ומבקשים את המשתנה API_KEY
#print(API_KEY)

#seesion -  הזמן שלנו כרגע באפליקציה - מהרגע שנכנסתי ועד שיצאתי אני בסשיין אחד

def start(): #פעם ראשונה שנכנסנו
    st.session_state.end=False
    st.session_state.gemini = genai.Client(api_key=API_KEY) #מתחברים עם הסיסמה שלנו
    st.session_state.history = [] #איפוס להיסטוריה
    message = send(prompt)  # שולחים לפונקציה
    #st.text(message)
    #תיבת טקסט של צאט
    #ai_text  = st.chat_message("ai")
    #ai_text.write(message)



#gemini = genai.Client(api_key=API_KEY) #

#הוראה -
prompt = """
    ###הקשר
    אנחנו במשחק "אליאס" - שזה משחק ניחושים
    עליך להגריל מילה ואני צריכה לנחש מה המילה שהגרלת
    אתה צריך לתת לי רמזים

    ###חוקים
    אסור שהמילה או השורש שלה יופיעו
    אל תגלה לי את המילה!
    כל פעם תן רמז אחד - הראשון יהיה כללי מאוד ואחר כך יותר ספציפי

    ###סיום משחק
    לאחר 3 נסיונות או הצלחה
    כתוב את המילה שהגרלת
    כתוב בסיום END
    נ.ב אתה יכול להגריל מילים של אוכל של זמרים מזרחיים של ארץ ישראל בדגש על זמרים מזרחיים(אם אתה שם זמר אז תכתוב אם הזמר ישן או חדש אם הוא מזרחית ישנה או חדשה אם הוא ממש  בוכה או רק עצוב וגם תן רמז שמאיפיין את הזמר עצמו )
"""

# מודלים
all_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash-lite"]



def send(prompt):

    st.session_state.history.append({   #שמירה של ההודעה של היוזר
            "sender": "user",
            "text": prompt
        })
    context = "זו השיחה המלאה: \n"
    for line in st.session_state.history:  #עבור כל שורה בהיסטוריה של הצ'אט
        context += f"{line['sender']}: {line['text']}\n" #תוסיף למשתנה

    with st.spinner("חושב..."):
        for model in all_models: #עובר על כל מודל ברשימה
            print(model)
            chat = st.session_state.gemini.chats.create(model=model) #לוקחים מסשיין את מה ששמור שם
            try: #לנסות
                message = chat.send_message(context)  # שולחים
                st.session_state.history.append({ #שמירה של ההודעה של הAI
                        "sender": "ai",
                        "text": message.text
                    })
               # print(st.session_state.history)
                return message.text #הצלחת לשלוח? תחזיר את התשובה
            except: #אם לא הצליח
                print("לא הצליח - מנסה את המודל הבא")

###לשים אחרי def send
if "gemini" not in st.session_state: #אם אין לך ג'מיני
    start() #תפעיל את ההתחלה

#else: #
    #אם זאת לא השיחה הראשונה

    if 'history' in st.session_state and len(st.session_state.history)>0:
        for line in st.session_state.history[1:]: #תתחיל ממקום מספר 1 - שזו ההודעה השניה
            chat = st.chat_message(line["sender"])
            chat.write(line["text"])
if 'end' in st.session_state and st.session_state.end:
    st.balloons()
    st.success("המשחק הסתיים")
#print("מתחיל...")
#chat = gemini.chats.create(model="gemini-2.0-flash") #יוצרים צ'אט חדש
#print("התחבר לג'מיני שולח הודעה...")

#message = chat.send_message(prompt) #שולחים
#message = send(prompt) #שולחים לפונקציה
#st.text(message)
else:
    user = st.chat_input("ניחוש")
    if user: #אם המשתמש ניחש
        #נכתוב את הניחוש על המסך
        user_text = st.chat_message("user")
        user_text.write(user)

        ai = send("הניחוש שלי: " + user)
        ai_text  = st.chat_message("ai")
        ai_text.write(ai)
        if 'END' in ai:
            st.session_state.end =True
            st.rerun()

# while True:
#     user = input("הניחוש שלך >> ")
#     message = send(prompt) #שולחים
#     print(message) #לראות מה חזר
#     if "END" in message:
#         break


#
# to = input("למי לכתוב ברכה? >> ")
# content = input("למתי הברכה? >> ")
# addons = input("מידע חשוב נוסף כדי לכתוב את הברכה >> ")
# # הנחייה לAI
# prompt = f""" אתה מומחה לכתיבת ברכות
#                 כתוב ברכה ל{to}
#                 לכבוד {content}
#                 שים לב ש {addons}
#                 עד 3 שורות, תוסיף אימוג'ים
#             """
# #print(API_KEY) בדיקה שמצא
# gemini = genai.Client(api_key=API_KEY) #יוצרת את החיבור - צד קליינט
# ai = gemini.chats.create(model="gemini-2.0-flash") #מודל gemini
# message = ai.send_message(prompt)
# print(message.text)
