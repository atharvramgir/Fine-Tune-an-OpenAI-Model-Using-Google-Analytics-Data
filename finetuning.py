from openai import OpenAI
client = OpenAI()

# client.files.create(
#   file=open("finetuning2.jsonl", "rb"),
#   purpose="fine-tune")

print(client.files.list())
client.fine_tuning.jobs.create(
   training_file="file-6XM4GFDsVvrmkQLQz9wdN0q4",
   model="gpt-4o-mini-2024-07-18"
 )

# List 10 fine-tuning jobs
print(client.fine_tuning.jobs.retrieve(fine_tuning_job_id="ftjob-8S5s8gZ96i63GU5X6ZTTRN98"))