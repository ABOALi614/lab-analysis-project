"""معلومات مبسطة عن كل حالة (للأغراض التعليمية فقط)."""

CONDITIONS = {
    "healthy": {
        "ar": {
            "name": "سليم (لا يوجد نمط أنيميا)",
            "what": "القيم دي أقرب لنمط الأشخاص الأصحاء في البيانات اللي اتدرب عليها الموديل، يعني مفيش نمط واضح لواحد من أنواع الأنيميا التلاتة التانية.",
            "pattern": "هيموجلوبين وحجم الكرية ضمن الحدود الطبيعية غالبًا.",
            "symptoms": [],
            "next": "",
            "note": "الموديل بيفرّق بين 4 حالات بس. مش بيكشف أمراض الدم التانية، وصحة الدم الكاملة بيحكم عليها الطبيب. لو عندك أعراض مستمرة (إرهاق، شحوب، دوخة) اعرض نفسك على الطبيب حتى لو النتيجة سليمة.",
        },
        "en": {
            "name": "Healthy (no anemia pattern)",
            "what": "These values are closest to the pattern of healthy people in the training data, so none of the three anemia patterns stands out.",
            "pattern": "Hemoglobin and red cell size are usually within normal limits.",
            "symptoms": [],
            "next": "",
            "note": "The model separates only 4 conditions. It does not detect other blood disorders, and a doctor judges overall blood health. If you have persistent symptoms (fatigue, pallor, dizziness), see a doctor even if the result looks healthy.",
        },
    },
    "iron_deficiency": {
        "ar": {
            "name": "أنيميا نقص الحديد (Iron Deficiency Anemia)",
            "what": "أنيميا بتحصل لما الجسم ما بيلاقيش حديد كفاية يصنع بيه الهيموجلوبين، فالكرات الحمراء بتطلع أصغر وأفتح من الطبيعي. من أشهر أنواع الأنيميا في العالم.",
            "pattern": "هيموجلوبين منخفض مع MCV وMCH وMCHC منخفضين (كرات صغيرة وباهتة)، وساعات الصفائح بتكون مرتفعة.",
            "symptoms": ["إرهاق وتعب عام", "شحوب في الوجه والجفون", "دوخة وصداع", "ضيق نفس مع المجهود", "خفقان", "تساقط الشعر وهشاشة الأظافر"],
            "next": "الطبيب بيأكد التشخيص عادة بتحليل الفيريتين ودراسة الحديد، ويدور على السبب (نزيف، قلة تغذية، سوء امتصاص). العلاج غالبًا مكملات حديد مع علاج السبب، وبقرار الطبيب فقط.",
        },
        "en": {
            "name": "Iron Deficiency Anemia",
            "what": "Anemia that happens when the body lacks enough iron to make hemoglobin, so red cells are smaller and paler than normal. It is one of the most common anemias worldwide.",
            "pattern": "Low hemoglobin with low MCV, MCH and MCHC (small, pale cells); platelets are sometimes raised.",
            "symptoms": ["Fatigue and weakness", "Pale skin and inner eyelids", "Dizziness and headache", "Shortness of breath on exertion", "Palpitations", "Hair loss and brittle nails"],
            "next": "A doctor usually confirms it with serum ferritin and iron studies and looks for the cause (bleeding, poor intake, poor absorption). Treatment is usually iron supplements plus treating the cause, decided by the doctor only.",
        },
    },
    "macrocytic": {
        "ar": {
            "name": "أنيميا كبيرة الكريات (Macrocytic Anemia)",
            "what": "أنيميا كرات الدم الحمراء فيها أكبر من الطبيعي. من أسبابها الشائعة نقص فيتامين B12 أو حمض الفوليك.",
            "pattern": "هيموجلوبين منخفض مع MCV مرتفع (أكتر من 100 fL تقريبًا).",
            "symptoms": ["إرهاق وضعف", "شحوب وأحيانًا اصفرار خفيف", "التهاب وألم في اللسان", "تنميل في الأطراف (مع نقص B12)", "صعوبة في التركيز والذاكرة"],
            "next": "الطبيب بيطلب غالبًا تحليل فيتامين B12 والفوليك، وفحص مسحة الدم، ويراجع أسباب تانية زي الكبد والغدة الدرقية وبعض الأدوية. العلاج بيعتمد على السبب.",
        },
        "en": {
            "name": "Macrocytic Anemia",
            "what": "Anemia in which red blood cells are larger than normal. Common causes include vitamin B12 or folate deficiency.",
            "pattern": "Low hemoglobin with high MCV (roughly above 100 fL).",
            "symptoms": ["Fatigue and weakness", "Pallor and sometimes mild jaundice", "Sore, inflamed tongue", "Tingling in hands and feet (with B12 deficiency)", "Difficulty concentrating, memory problems"],
            "next": "A doctor usually orders vitamin B12 and folate levels and a blood smear, and checks other causes such as liver disease, thyroid problems and some medicines. Treatment depends on the cause.",
        },
    },
    "normocytic_normochromic": {
        "ar": {
            "name": "أنيميا طبيعية الكريات والصبغة (Normocytic Normochromic Anemia)",
            "what": "أنيميا حجم الكرية فيها وتركيز الهيموجلوبين طبيعيين تقريبًا، لكن العدد أو كمية الهيموجلوبين الكلية قليلة. بتبقى غالبًا نتيجة لسبب تاني مش مشكلة في الغذاء بس.",
            "pattern": "هيموجلوبين منخفض مع MCV وMCHC في الحدود الطبيعية.",
            "symptoms": ["إرهاق وتعب", "شحوب", "ضيق نفس مع المجهود", "دوخة", "أعراض المرض الأساسي لو موجود"],
            "next": "من أسبابها الأمراض المزمنة والالتهابات، وأمراض الكلى، والنزيف الحاد، وبعض مشاكل النخاع. الطبيب بيطلب تحاليل زي الريتيكيولوسايت (الكرات الشبكية) ووظائف الكلى ودراسة الحديد عشان يحدد السبب.",
        },
        "en": {
            "name": "Normocytic Normochromic Anemia",
            "what": "Anemia in which cell size and hemoglobin concentration are about normal, but the number of red cells or total hemoglobin is low. It is often a consequence of another condition rather than diet alone.",
            "pattern": "Low hemoglobin with MCV and MCHC within normal limits.",
            "symptoms": ["Fatigue and weakness", "Pallor", "Shortness of breath on exertion", "Dizziness", "Symptoms of the underlying disease, if present"],
            "next": "Causes include chronic disease and inflammation, kidney disease, acute blood loss and some bone marrow problems. A doctor orders tests such as reticulocyte count, kidney function and iron studies to find the cause.",
        },
    },
}
