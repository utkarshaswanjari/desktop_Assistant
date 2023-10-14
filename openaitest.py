import os
import openai
from config import apikey

openai.api_key = apikey



openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to company for resignation\n\n<Dear [NAME],\n\nI am writing to formally resign from my position as [POSITION] with [COMPANY NAME]. My final day of employment will be [LAST DAY YOU PLAN TO WORK], [DATE].\n\nI would like to take this opportunity to thank you and the entire team for the support and mentorship you offered me during my time at [COMPANY NAME]. I have learned a great deal while in this position and am grateful for the experience.\n\nI intend to finish out my employment in a professional and efficient manner and am available to assist with any transition needs.\n\nAgain, I thank you for the opportunity and wish the team all the best in future endeavors.\n\nSincerely,\n\n[YOUR NAME]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company], and I am grateful for the opportunity to work here. I have learned a great deal during my time in this position, and I am grateful for the experience.\n\nIf I can be of any assistance during this transition, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1683815400,
  "id": "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",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 125,
    "prompt_tokens": 9,
    "total_tokens": 134
  }
}
'''