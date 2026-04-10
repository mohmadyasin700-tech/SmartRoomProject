import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="Idris Smart Systems",
    page_icon="🛡️",
    layout="centered"
)

# العنوان الرئيسي
st.title("🌐 لوحة التحكم في الغرفة الذكية")
st.markdown("---")

# القائمة الجانبية (Sidebar) للتحكم
st.sidebar.header("⚙️ إعدادات النظام")
safe_mode = st.sidebar.toggle("تفعيل وضع الأمان الإقليمي", value=True)
limit_temp = st.sidebar.slider("حد تنبيه الحرارة (م°)", 18, 40, 25)

# القسم الأول: المدخلات (الحساسات)
st.subheader("📊 قراءات الحساسات الحالية")
col_input1, col_input2 = st.columns(2)

with col_input1:
    motion = st.checkbox("🚶 رصد حركة داخل الغرفة")
    
with col_input2:
    current_temp = st.number_input("🌡️ درجة الحرارة المسجلة", value=22)

st.divider()

# القسم الثاني: المعالجة الذكية والمخرجات
st.subheader("🖥️ حالة الأجهزة والمخرجات")
c1, c2, c3 = st.columns(3)

# 1. نظام الإضاءة الذكي
if motion:
    c1.success("💡 الإضاءة\n\nتعمل (ON)")
else:
    c1.info("🌑 الإضاءة\n\nمطفأة (OFF)")

# 2. نظام التكييف الذكي
if current_temp > limit_temp:
    c2.warning(f"❄️ التكييف\n\nيعمل (تبريد)")
else:
    c2.info("🌡️ التكييف\n\nفي وضع الاستعداد")

# 3. نظام الأمان المتطور
if safe_mode and motion:
    c3.error("🚨 الأمن\n\nتنبيه: حركة مشبوهة!")
    st.snow()  # تأثير بصري عند رصد اختراق
elif not safe_mode:
    c3.disable("🔓 الأمن\n\nالنظام معطل")
else:
    c3.success("🛡️ الأمن\n\nالموقع آمن")

# القسم الثالث: سجل العمليات (Logs)
st.markdown("---")
if st.button("💾 حفظ الحالة الحالية في السجل"):
    status = "آمن" if not (safe_mode and motion) else "تنبيه أمني"
    st.write(f"✅ **تم التسجيل:** حرارة {current_temp}° | حركة: {motion} | الحالة: {status}")
