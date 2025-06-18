# check if it's  a LOGIN action and extract the id

raw_record = "  userID:john_doe_123, Action:LOGIN, status:Success   "

# Step 1 & 2: Clean and normalize the record
marker_start_text = "userid:"
processed_record = raw_record.strip().lower()
# processed_record is now "userid:john_doe_123, action:login, status:success" , remove whitespace using strip({automatically a whitespace}), then lowered.

# Step 3: Check if the action was a "login"
is_login_action = "action:login" in processed_record
print(f"Is it a login action? {is_login_action}")

# Step 4: Extract the userID
# Find where the actual ID starts (right after "userid:")
id_starts_at = processed_record.find(marker_start_text) + len(marker_start_text)

# Find where the ID ends (at the first comma after the ID starts)
id_ends_before = processed_record.find(
    ",", id_starts_at
)  # Start searching for comma from where ID begins

# Perform the slice
if (
    id_starts_at != -1 + len(marker_start_text) and id_ends_before != -1
):  # Check if markers were found
    user_id_value = processed_record[id_starts_at:id_ends_before]
    print(f"Extracted userID: {user_id_value}")
else:
    print("Could not extract userID. Check markers.")
