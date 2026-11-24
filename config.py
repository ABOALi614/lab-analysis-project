# ------------------------------------------------------------
# ملف الإعدادات: غيّر الاسم والروابط من هنا فقط
# Settings file: edit the name and links here only
# ------------------------------------------------------------

AUTHOR_NAME_AR = "أحمد عبدالجيد"
AUTHOR_NAME_EN = "Ahmed Abd-Algayed"

LINKS = {
    "Facebook": "https://www.facebook.com/ahmmedhmaid",
    "Instagram": "https://www.instagram.com/ahmed_hmaid_1/",
    "GitHub": "https://github.com/ABOALi614",
}

# أقل نسبة ثقة نعتبر عندها النتيجة "مقبولة" (من 0 إلى 1)
LOW_CONFIDENCE_THRESHOLD = 0.60

# ترتيب ظهور الخانات في الصفحة (لازم تتطابق مع FEATURES في نوتبوك التدريب)
FEATURE_ORDER = ["HGB", "RBC", "HCT", "WBC", "MCV", "MCH", "MCHC", "PLT"]

# بيانات كل قياس:
#   unit    = الوحدة
#   dec     = عدد الأرقام العشرية
#   ref     = المدى الطبيعي للبالغين (M ذكر / F أنثى) — للعرض والمقارنة فقط
#   hard    = أوسع مدى معقول (أي قيمة برا المدى ده غالبًا غلطة كتابة)
FEATURE_INFO = {
    "HGB":  {"ar": "الهيموجلوبين", "en": "Hemoglobin", "unit": "g/dL", "dec": 1,
             "ref": {"M": (13.5, 17.5), "F": (12.0, 15.5)}, "hard": (2.0, 25.0)},
    "RBC":  {"ar": "كرات الدم الحمراء", "en": "Red blood cells", "unit": "×10⁶/µL", "dec": 2,
             "ref": {"M": (4.5, 5.9), "F": (4.1, 5.1)}, "hard": (0.5, 9.0)},
    "HCT":  {"ar": "الهيماتوكريت", "en": "Hematocrit", "unit": "%", "dec": 1,
             "ref": {"M": (41.0, 53.0), "F": (36.0, 46.0)}, "hard": (5.0, 70.0)},
    "WBC":  {"ar": "كرات الدم البيضاء", "en": "White blood cells", "unit": "×10³/µL", "dec": 1,
             "ref": {"M": (4.0, 11.0), "F": (4.0, 11.0)}, "hard": (0.1, 500.0)},
    "MCV":  {"ar": "متوسط حجم الكرية", "en": "Mean cell volume", "unit": "fL", "dec": 1,
             "ref": {"M": (80.0, 100.0), "F": (80.0, 100.0)}, "hard": (40.0, 150.0)},
    "MCH":  {"ar": "متوسط هيموجلوبين الكرية", "en": "Mean cell hemoglobin", "unit": "pg", "dec": 1,
             "ref": {"M": (27.0, 33.0), "F": (27.0, 33.0)}, "hard": (10.0, 50.0)},
    "MCHC": {"ar": "تركيز هيموجلوبين الكرية", "en": "Mean cell Hb concentration", "unit": "g/dL", "dec": 1,
             "ref": {"M": (32.0, 36.0), "F": (32.0, 36.0)}, "hard": (20.0, 45.0)},
    "PLT":  {"ar": "الصفائح الدموية", "en": "Platelets", "unit": "×10³/µL", "dec": 0,
             "ref": {"M": (150.0, 450.0), "F": (150.0, 450.0)}, "hard": (1.0, 2000.0)},
}
