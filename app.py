import streamlit as st
import re
import random
import string

# -------------------------------------
# Page Setup
# -------------------------------------
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Checker")

# -------------------------------------
# Password Input
# -------------------------------------
password = st.text_input("Enter your password", type="password")

# -------------------------------------
# Password Strength Logic
# -------------------------------------
score = 0
suggestions = []

if password:
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("• Use at least 8 characters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("• Add uppercase letters")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("• Add lowercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("• Include numbers")

    if any(char in "!@#$%^&*" for char in password):
        score += 1
    else:
        suggestions.append("• Add special characters (!@#$%^&*)")

    # -------------------------------------
    # Display Strength
    # -------------------------------------
    strength_percent = int((score / 5) * 100)
    st.progress(strength_percent)

    if score <= 2:
        st.error("Weak Password ❌")
    elif score <= 4:
        st.warning("Moderate Password ⚠️")
    else:
        st.success("Strong Password ✔️")

    # -------------------------------------
    # Suggestions
    # -------------------------------------
    if suggestions:
        st.write("### Suggestions to improve:")
        for tip in suggestions:
            st.write(tip)
    else:
        st.write("Great job! Your password is strong.")

# -------------------------------------
# Password Generator
# -------------------------------------
if st.button("Generate Strong Password"):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    generated = "".join(random.choice(chars) for _ in range(12))
    st.success(f"Generated Password: {generated}")