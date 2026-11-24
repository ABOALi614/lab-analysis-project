"""الموقع الرئيسي — شغّله بالأمر:  streamlit run app.py"""
from html import escape

import streamlit as st

from condition_info import CONDITIONS
from config import (AUTHOR_NAME_AR, AUTHOR_NAME_EN, FEATURE_INFO, FEATURE_ORDER, LINKS,
                    LOW_CONFIDENCE_THRESHOLD)
from model_utils import (load_model_and_meta, model_files_exist, predict, sklearn_mismatch)
from translations import TEXTS

st.set_page_config(page_title="CBC Analyzer", page_icon="🩸", layout="wide")

# ---------------- اللغة والتنقل ----------------
lang_choice = st.sidebar.radio("🌐 اللغة / Language", ["العربية", "English"], horizontal=True)
lang = "ar" if lang_choice == "العربية" else "en"
t = TEXTS[lang]

page = st.sidebar.radio(t["nav"], ["home", "about"], format_func=lambda k: t["nav_" + k], key="page")
st.sidebar.info(t["disclaimer"])

# ---------------- الشكل (CSS) ----------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
html, body, .stApp, .stMarkdown, button, label, p, li, h1, h2, h3, h4, input, td, th {
    font-family: 'IBM Plex Sans Arabic', 'Segoe UI', Tahoma, sans-serif;
}
__RTL__
#MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1060px; padding-top: 2rem; padding-bottom: 3rem; }
h2, h3 { color: #12303B; font-weight: 600; }

.hero { background: #12303B; color: #fff; border-radius: 14px; padding: 1.8rem 2rem; margin-bottom: 1.6rem;
        display: flex; gap: 1.2rem; align-items: center; }
.hero svg { flex: 0 0 auto; }
.hero h1 { color: #fff; font-size: 1.9rem; font-weight: 700; line-height: 1.35; margin: 0 0 .35rem; padding: 0; }
.hero p { color: #C9DADF; margin: 0; line-height: 1.8; max-width: 52rem; }

.panel { background: #fff; border: 1px solid #D5DFE3; border-radius: 12px; padding: 1.2rem 1.4rem; margin-bottom: 1.2rem; }
.hint { color: #52707A; font-size: .92rem; margin: -.2rem 0 .9rem; }
.pname-cap { color: #52707A; font-size: .82rem; margin-top: -.55rem; margin-bottom: .6rem; }

.res { display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; border-inline-start: 6px solid #A4262C; }
.res .lbl { color: #52707A; font-size: .9rem; }
.res .name { font-size: 1.55rem; font-weight: 700; color: #12303B; line-height: 1.5; }
.res .conf { margin-inline-start: auto; text-align: center; min-width: 120px; }
.res .conf .num { font-size: 2.2rem; font-weight: 700; color: #A4262C; line-height: 1.1; direction: ltr; }

.tablewrap { overflow-x: auto; }
table.lab { width: 100%; border-collapse: collapse; font-size: .95rem; }
table.lab th { text-align: center; color: #52707A; font-weight: 500; border-bottom: 2px solid #12303B; padding: .5rem .6rem; white-space: nowrap; }
table.lab td { border-bottom: 1px solid #E3EAED; padding: .6rem .6rem; vertical-align: middle; }
table.lab .sub { color: #52707A; font-size: .82rem; }
table.lab .num { direction: ltr; text-align: center; white-space: nowrap; font-variant-numeric: tabular-nums; }
table.lab th:first-child { text-align: start; }
.unit { color: #52707A; font-size: .8rem; }
.track { position: relative; height: 8px; border-radius: 4px; background: #E3EAED; min-width: 130px; direction: ltr; }
.zone { position: absolute; top: 0; bottom: 0; background: #A9D3C3; border-radius: 4px; }
.mark { position: absolute; top: -4px; width: 16px; height: 16px; border-radius: 50%; background: #12303B;
        border: 3px solid #fff; box-shadow: 0 0 0 1px #12303B; transform: translateX(-50%); }
.mark.low, .mark.high { background: #A4262C; box-shadow: 0 0 0 1px #A4262C; }
.badge { display: inline-block; padding: .1rem .65rem; border-radius: 999px; font-size: .85rem; font-weight: 600; }
.badge.ok { background: #E3F2EC; color: #1E6B4D; }
.badge.low, .badge.high { background: #F8E3E4; color: #8E1F25; }
.refnote { color: #52707A; font-size: .85rem; margin-top: .7rem; }

.prow { display: flex; align-items: center; gap: .8rem; margin: .55rem 0; }
.pname { flex: 0 0 38%; font-size: .95rem; }
.pbar { flex: 1; height: 10px; background: #E3EAED; border-radius: 5px; overflow: hidden; direction: ltr; }
.pfill { height: 100%; background: #9DB4BC; border-radius: 5px; }
.pfill.top { background: #A4262C; }
.pval { flex: 0 0 4.2rem; text-align: end; direction: ltr; font-variant-numeric: tabular-nums; color: #12303B; }

.info h4 { margin: 1rem 0 .3rem; color: #12303B; font-size: 1rem; font-weight: 600; }
.info p { margin: 0; line-height: 1.9; }
.info ul { margin: 0; padding-inline-start: 1.3rem; line-height: 1.9; }
.note { background: #FFF6E5; border: 1px solid #F0D8A8; border-radius: 10px; padding: .8rem 1rem; margin-top: 1rem; line-height: 1.9; }

.author-card { margin-top: 2.5rem; padding: 1.2rem 1rem; border-radius: 14px; text-align: center; background: #12303B; color: #fff; }
.author-card .name { font-size: 1.2rem; font-weight: 700; margin: .2rem 0 .8rem; }
.author-card a { display: inline-block; margin: .2rem .3rem; padding: .35rem .9rem; border-radius: 999px;
                 background: rgba(255,255,255,.14); color: #fff !important; text-decoration: none; font-weight: 600; }
.author-card a:hover { background: rgba(255,255,255,.28); }
@media (max-width: 640px) {
  .hero { flex-direction: column; align-items: flex-start; padding: 1.3rem; }
  .hero h1 { font-size: 1.45rem; }
  .res .conf { margin-inline-start: 0; }
  .pname { flex-basis: 45%; }
}
</style>
"""
RTL_CSS = """
.block-container, [data-testid="stSidebarUserContent"] { direction: rtl; text-align: right; }
""" if lang == "ar" else ""
st.markdown(CSS.replace("__RTL__", RTL_CSS), unsafe_allow_html=True)

DROP_SVG = (
    '<svg width="54" height="54" viewBox="0 0 64 64" aria-hidden="true">'
    '<path d="M32 4C32 4 12 28 12 42a20 20 0 0 0 40 0C52 28 32 4 32 4z" fill="#A4262C"/>'
    '<path d="M22 42a10 10 0 0 0 8 9.8" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".55"/>'
    "</svg>"
)


# ---------------- دوال مساعدة ----------------
def fmt(v, dec):
    return f"{v:.{dec}f}"


def ref_range(f, sex):
    return FEATURE_INFO[f]["ref"][sex]


def status_of(v, lo, hi):
    return "low" if v < lo else ("high" if v > hi else "ok")


def range_bar(v, lo, hi, status):
    span = hi - lo
    smin = max(lo - span * 0.9, 0.0)
    smax = hi + span * 0.9
    scale = smax - smin
    pos = (min(max(v, smin), smax) - smin) / scale * 100
    z0 = (lo - smin) / scale * 100
    z1 = (hi - smin) / scale * 100
    return (f'<div class="track"><div class="zone" style="left:{z0:.1f}%;width:{z1 - z0:.1f}%"></div>'
            f'<div class="mark {status}" style="left:{pos:.1f}%"></div></div>')


def inconsistent(v):
    """MCV=HCT/RBC*10 ، MCH=HGB/RBC*10 ، MCHC=HGB/HCT*100 — لو الفرق كبير الأرقام غالبًا فيها غلط."""
    calc = {"MCV": v["HCT"] / v["RBC"] * 10, "MCH": v["HGB"] / v["RBC"] * 10, "MCHC": v["HGB"] / v["HCT"] * 100}
    return [k for k, c in calc.items() if abs(c - v[k]) / c > 0.15]


def input_key(f):
    return f"in_{f}"


def clear_all():
    for f in FEATURE_ORDER:
        st.session_state[input_key(f)] = None
    st.session_state.pop("result", None)


def load_example(cls, meta):
    for f, val in meta["examples"][cls].items():
        st.session_state[input_key(f)] = round(float(val), FEATURE_INFO[f]["dec"])
    st.session_state.pop("result", None)


def author_card():
    name = AUTHOR_NAME_AR if lang == "ar" else AUTHOR_NAME_EN
    links = "".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
        for label, url in LINKS.items() if url
    )
    st.markdown(
        f'<div class="author-card"><div>{t["built_by"]}</div><div class="name">{name}</div>'
        f'<div>{t["follow_me"]}</div><div>{links}</div></div>',
        unsafe_allow_html=True,
    )


def bullets(items):
    return "<ul>" + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


# ---------------- عرض النتيجة ----------------
def render_result(res, meta):
    vals, probs, top, conf = res["values"], res["probs"], res["top"], res["conf"]
    sex = res["sex"]
    info = CONDITIONS.get(top, {}).get(lang, {"name": top, "what": "", "pattern": "", "symptoms": [], "next": ""})

    st.subheader(t["result_title"])
    st.markdown(
        f'<div class="panel res"><div><div class="lbl">{t["predicted"]}</div>'
        f'<div class="name">{escape(info["name"])}</div></div>'
        f'<div class="conf"><div class="lbl">{t["confidence"]}</div><div class="num">{conf * 100:.1f}%</div></div></div>',
        unsafe_allow_html=True,
    )
    if conf < LOW_CONFIDENCE_THRESHOLD:
        st.warning(t["low_conf"])

    # جدول شبه ورقة المعمل
    rows = ""
    for f in FEATURE_ORDER:
        fi = FEATURE_INFO[f]
        v = vals[f]
        lo, hi = ref_range(f, sex)
        s = status_of(v, lo, hi)
        d = fi["dec"]
        rows += (
            f'<tr><td><b>{f}</b><br><span class="sub">{escape(fi[lang])}</span></td>'
            f'<td class="num"><b>{fmt(v, d)}</b> <span class="unit">{escape(fi["unit"])}</span></td>'
            f'<td class="num">{fmt(lo, d)} – {fmt(hi, d)}</td>'
            f'<td>{range_bar(v, lo, hi, s)}</td>'
            f'<td><span class="badge {s}">{t["st_" + s]}</span></td></tr>'
        )
    head = "".join(f"<th>{t[k]}</th>" for k in ("col_param", "col_value", "col_ref", "col_range", "col_status"))
    st.markdown(f"**{t['report_title']}**")
    st.markdown(
        f'<div class="panel"><div class="tablewrap"><table class="lab"><thead><tr>{head}</tr></thead>'
        f'<tbody>{rows}</tbody></table></div><div class="refnote">{t["ref_note"]}</div></div>',
        unsafe_allow_html=True,
    )

    # احتمالات الحالات
    prow = ""
    for c, p in sorted(probs.items(), key=lambda kv: -kv[1]):
        nm = CONDITIONS.get(c, {}).get(lang, {}).get("name", c)
        cls = "pfill top" if c == top else "pfill"
        prow += (f'<div class="prow"><div class="pname">{escape(nm)}</div>'
                 f'<div class="pbar"><div class="{cls}" style="width:{p * 100:.1f}%"></div></div>'
                 f'<div class="pval">{p * 100:.1f}%</div></div>')
    st.markdown(f"**{t['probs_title']}**")
    st.markdown(f'<div class="panel">{prow}</div>', unsafe_allow_html=True)

    # معلومات الحالة
    st.subheader(t["about_condition"])
    body = ""
    if info.get("what"):
        body += f'<h4>{t["what_is"]}</h4><p>{escape(info["what"])}</p>'
    if info.get("pattern"):
        body += f'<h4>{t["pattern"]}</h4><p>{escape(info["pattern"])}</p>'
    if info.get("symptoms"):
        body += f'<h4>{t["symptoms"]}</h4>{bullets(info["symptoms"])}'
    if info.get("next"):
        body += f'<h4>{t["next_step"]}</h4><p>{escape(info["next"])}</p>'
    if info.get("note"):
        body += f'<div class="note"><b>{t["note"]}:</b> {escape(info["note"])}</div>'
    st.markdown(f'<div class="panel info">{body}</div>', unsafe_allow_html=True)
    st.warning(t["disclaimer"])


# ---------------- صفحة التحليل ----------------
def home_page():
    st.markdown(
        f'<div class="hero">{DROP_SVG}<div><h1>{t["app_title"]}</h1><p>{t["app_subtitle"]}</p></div></div>',
        unsafe_allow_html=True,
    )

    if not model_files_exist():
        st.error(t["model_missing"])
        return
    try:
        model, meta = load_model_and_meta()
    except Exception as e:  # noqa: BLE001
        st.error(f"{t['model_error']}\n\n`{type(e).__name__}: {e}`")
        return
    if set(meta["features"]) != set(FEATURE_ORDER):
        st.error("model_meta.json features do not match config.FEATURE_ORDER")
        return
    mm = sklearn_mismatch(meta)
    if mm:
        st.warning(t["version_warn"].format(trained=mm[0], installed=mm[1]))

    st.subheader(t["inputs_title"])
    st.markdown(f'<div class="hint">{t["inputs_hint"]}</div>', unsafe_allow_html=True)

    st.radio(t["sex_label"], ["M", "F"], format_func=lambda k: t["sex_" + k], horizontal=True, key="sex")
    sex = st.session_state.get("sex", "M")

    values = {}
    for row in (FEATURE_ORDER[:4], FEATURE_ORDER[4:]):
        cols = st.columns(4)
        for col, f in zip(cols, row):
            fi = FEATURE_INFO[f]
            lo, hi = ref_range(f, sex)
            d = fi["dec"]
            with col:
                values[f] = st.number_input(
                    f"{f} ({fi['unit']})",
                    min_value=float(fi["hard"][0]), max_value=float(fi["hard"][1]),
                    value=None, step=10.0 ** (-d) if d else 1.0, format=f"%.{d}f",
                    key=input_key(f), placeholder=f"{fmt(lo, d)} – {fmt(hi, d)}",
                )
                st.markdown(f'<div class="pname-cap">{escape(fi[lang])}</div>', unsafe_allow_html=True)

    st.markdown(f"**{t['examples_title']}**")
    classes = list(meta["examples"].keys())
    cols = st.columns(len(classes) + 1)
    for col, c in zip(cols, classes):
        nm = CONDITIONS.get(c, {}).get(lang, {}).get("name", c).split(" (")[0]
        col.button(t["example_btn"].format(name=nm), key=f"ex_{c}", on_click=load_example,
                   args=(c, meta), use_container_width=True)
    cols[-1].button(t["clear_btn"], key="clear", on_click=clear_all, use_container_width=True)

    if st.button(t["analyze_btn"], type="primary", use_container_width=True):
        missing = [f for f in FEATURE_ORDER if values[f] is None]
        if missing:
            st.error(t["fill_all"].format(names=", ".join(missing)))
            st.session_state.pop("result", None)
        else:
            with st.spinner(t["analyzing"]):
                top, conf, probs = predict(values)
            st.session_state["result"] = {"values": dict(values), "sex": sex, "top": top, "conf": conf, "probs": probs}

    res = st.session_state.get("result")
    if res:
        v = res["values"]
        bad = inconsistent(v)
        if bad:
            st.warning(t["consistency_warn"].format(names=", ".join(bad)))
        outside = [f for f in FEATURE_ORDER
                   if not (meta["ranges"][f][0] <= v[f] <= meta["ranges"][f][1])]
        if outside:
            st.warning(t["range_warn"].format(names=", ".join(outside)))
        render_result(res, meta)


# ---------------- صفحة عن المشروع ----------------
def about_page():
    st.title(t["about_title"])
    st.write(t["about_intro"])
    st.subheader(t["about_how_title"])
    st.markdown("\n".join(f"{i}. {s}" for i, s in enumerate(t["about_how"], 1)))
    st.subheader(t["about_data_title"])
    st.write(t["about_data"])
    st.subheader(t["about_model_title"])
    st.write(t["about_model"])
    st.subheader(t["about_limits_title"])
    st.markdown("\n".join(f"- {i}" for i in t["about_limits"]))
    st.warning(t["disclaimer"])


if page == "home":
    home_page()
else:
    about_page()

author_card()
