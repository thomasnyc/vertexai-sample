import vertexai
from vertexai.generative_models import GenerativeModel

# need to run this: pip install --upgrade google-cloud-aiplatform

# TODO(developer): Update project_id
# PROJECT_ID = "your-project-id"
vertexai.init(project="thomashk-mig", location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

response = model.generate_content(
    "What's a good name for new website sells raspberry Pi and add-ons"
)

print(response.text)
