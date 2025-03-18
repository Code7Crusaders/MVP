class PromptTemplateModel():
    def __init__(self, prompt_template_content: str):
        self.prompt_template_content = prompt_template_content

    def get_prompt_template_content(self):
        return self.prompt_template_content