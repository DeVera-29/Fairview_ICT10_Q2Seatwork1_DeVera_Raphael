from pyscript import document, display

club_members = ["Tom Pearl", "Bill Urine", "Big goy"]

def check_candidate(e):
    
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}"

    is_member = full_name in club_members

    messages = [
        f"Sorry {full_name}, you are not on the list.",
        f"Congratulations {full_name}! You are now in Rainbow Catering."
    ]

    result_message = messages[int(is_member)]

    # clear result and show new message
    document.getElementById("result").innerHTML = ""
    display(result_message, target="result")