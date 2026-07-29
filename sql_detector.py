filename = input("Enter the filename to scan for SQL injection vulnerabilities: ")

try:
    with open(filename, 'r') as file:
        code = file.read()
 
    print("File loaded successfully.")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
    exit()

print("\n========== Code Content ==========")
print(code)

print("\n========== Scan Report ==========")

lines = code.splitlines()
found = False
vulnerability_count = 0

for line_number, line in enumerate(lines, start=1):
    upper_line = line.upper()

    for keyword in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
        if keyword in upper_line:
            print(f"🔍 SQL keyword found: {keyword} on line {line_number}")

            if "+" in line:
                print(f"⚠️ Possible SQL Injection on line {line_number}")
                found = True
                vulnerability_count += 1

if not found:
    print("✅ No obvious SQL Injection vulnerability detected.")
    
print("\n========== Summary ==========")
print(f"Total vulnerabilities found: {vulnerability_count}")

print("\n========== Risk Level ==========")

if vulnerability_count == 0:
    print("🟢 Risk Level: LOW")
elif vulnerability_count <= 2:
    print("🟡 Risk Level: MEDIUM")
else:
    print("🔴 Risk Level: HIGH")

print("\n========== Recommendation ==========")

if found and "+" in code:
    print("Use parameterized queries instead of string concatenation.")
    print("Avoid directly inserting user input into SQL queries.")
else:
    print("No recommendations. Code appears safe from this basic check.")
