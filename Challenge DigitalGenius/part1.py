import pandas as pd
import numpy as np

if __name__ == '__main__':
	print("extracting messages, please wait...")
	path = "../../data/"

	df = pd.read_csv(path+"emails.csv")

	df["date"] = df["message"].map(lambda x : x.split("\n")[1][5:])
	df["sender"] = df["message"].map(lambda x : x.split("\n")[2][5:].strip())
	df["receiver"] = df["message"].map(lambda x : x.split("\n")[3][3:].strip())
	df["subject"] = df["message"].map(lambda x : x.split("\n")[4][7:].strip())
	df["content"] = df["message"].map(lambda x : " ".join(x.split("X-")[-1].split("\n")[1:]))
	df["date"] = pd.to_datetime(df["date"])
	df["time"] = df["date"].map(lambda x : x.time())
	df["date"] = df["date"].map(lambda x : x.date())

	df.drop(["message", "file"], axis=1, inplace=True)

	df.to_csv(path+"emails_clean.csv")
	print("Successful Extraction, Please run part2.py for the API")
	print(df.head())