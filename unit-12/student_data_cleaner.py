# registraton field date
raw_name = "   Choicey OSARO   "
raw_email = "   CHOICEYotas@gmail.com  "
raw_phone = "   090-34-65-634   "

clean_name = raw_name.strip().title()
clean_email = raw_email.strip().lower()
clean_phone = raw_phone.replace(",", "")

print(f"Name : {clean_name}")
print(f"Email : {clean_email}")
print(f"Phone : {clean_phone}")

print(f"Name length valid (>3): {len(clean_name) > 3}")
print(f"Email contains @: {"@" in clean_email}")
