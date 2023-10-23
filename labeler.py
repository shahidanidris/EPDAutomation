import pandas as pd
import os

df = pd.read_csv("dataframe.csv")

if os.path.exists("dataframe_labeled.csv"):
    output_df = pd.read_csv("dataframe_labeled.csv")
else:
    output_df = pd.DataFrame(
        columns=['text','failureCat']
    )
    output_df.to_csv("dataframe_labeled.csv")

list_x = list(df['text'])

# Filter the DataFrame by the values in column B
filtered_df = output_df[output_df['failureCat'].isna()]
filtered_df_list_x = list(filtered_df['text'])

output_df_list_x = list(output_df['text'])

failureCat = {
    0: "",
    1: "TX/Sensor Drift",
    2: "TX/Sensor Out of Range",
    3: "TX/Sensor Reading Mismatch/Not Tally with Reference",
    4: "TX/Sensor Reading Undefined",
    5: "TX/Sensor Reading Fluctuate",
    6: "TX/Sensor Reading Freeze",
    7: "TX/Sensor Intermittent Fault",
    8: "TX/Sensor damaged/faulty",
    9: "TX/Sensor Loop Connection Issue",
    10: "TX/Sensor Accessories (Rotameter, Display, Gauge, etc) Faulty",
    11: "Analyser reagent/solution low",
    12: "Valve body damaged",
    13: "Valve regulator faulty",
    14: "Valve jerking (rapid open/close)",
    15: "Valve stuck (unable to open/close)",
    16: "Valve position/indication mismatch with site",
    17: "Manifold damaged/faulty/leaking/passing",
    18: "Valve leaking/passing",
    19: "Valve Clogged",
    20: "Instrument Grounding Cable Damaged",
    21: "Non-Failure",
    22: "CLOSE"
}

x_toadd = []

# Compare Labeled CSV with Unlabeled CSV
for element in list_x:
    if element not in output_df_list_x or element in filtered_df_list_x:
        x = element
        os.system("cls")
        print(x)
        print()
        for key, values in failureCat.items():
            print(f"{key}: {values}")
        print()
        y = -1
        while y < 0 or y > 22:
            y = int(input("Label: "))
        print()
        if y == 22:
            break
        else:
            output_df = output_df.append({'text': x, 'failureCat': failureCat.get(y)}, ignore_index=True)

output_df = output_df.drop_duplicates(subset=['text'], keep='last')
output_df.to_csv("dataframe_labeled.csv", index=False)