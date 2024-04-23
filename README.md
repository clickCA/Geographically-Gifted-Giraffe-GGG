## **Project: Geographically Gifted Giraffe (GGG)**

Team members:

-   member1: 6330281421, นันทวัฒน์, รัตนธน
-   member2: 6330078421, ชนากร, อร่ามศักดิ์
-   member3: 6330212121, ธนกฤต, เป็นทุน

## **Problem Statement:**

Travelers often lack engaging and accessible resources to learn about destinations. Traditional guidebooks are static and bulky, while online resources can be overwhelming. GGG aims to bridge this gap by offering a fun and interactive way to explore the world through a friendly chatbot.

**Entertainment Value:**

-   **GGG's Quirky Personality:** Infuse GGG's responses with humor, trivia, and unexpected facts to make learning about travel enjoyable.
-   **Interactive Learning:** Allow users to ask questions and discover information through a conversational format.
-   **Image Recognition Fun:** Turn landmark identification into some knowledge, encouraging users to explore photos from their travels.

---

## **Approach:**

-   **Core Technology:**
    -   **Cloud Vision API:** Integrate Google Cloud's Vision API for basic image recognition, allowing users to identify landmarks through photos.
    -   **Large Language Model (LLM):** Utilize Google AI's Gemini to provide informative and engaging responses to user travel inquiries.
    -   **Google Cloud Text-to-Speech API** (Text-to-Speech Conversion) - This will convert GGG's responses into natural-sounding speech, enhancing the user experience.
-   **Focus on a Limited Set:** Initially focus on a curated list of popular travel destinations and highly recognizable landmarks to ensure accurate information and limit development time.

## Before Starting:

```python
pip install -r requirements.txt
```

run the server:

```python
uvicorn main:app --reload
```

you can see swagger in [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
