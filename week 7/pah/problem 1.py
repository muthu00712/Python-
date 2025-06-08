import pandas as pd
import sys
n = int(input())
records = []
for _ in range(n):
 line = sys.stdin.readline()
 parts = line.rstrip('\n').split(' ', 1)
 respondent_id = parts[0]
 feedback = parts[1] if len(parts) > 1 and parts[1].strip() else 'No Response'
 records.append((respondent_id, feedback))
df = pd.DataFrame(records, columns=["RespondentID", "Feedback"])
print("Survey Responses with Missing Feedback Filled:")
print(df.to_string(index=False))