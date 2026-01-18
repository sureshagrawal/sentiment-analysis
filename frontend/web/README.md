# Frontend – Sentiment Analysis UI

This directory contains the **frontend web application** for the Sentiment Analysis system.

The UI is designed to be:
- Clean
- Responsive
- Confidence-aware
- User-friendly

---

## ✨ Key Features

- Text input for sentiment analysis
- Animated confidence bar
- Emoji-based sentiment feedback
- Gradient-based premium UI
- Mobile-first responsive design

---

## 🛠 Tech Stack

- Next.js (App Router)
- Tailwind CSS
- JavaScript (no TypeScript)
- Fetch API for backend communication

---

## 🔁 API Integration

The frontend consumes the backend API using a standardized response schema.

### Example Response
```json
{
  "status": "success",
  "data": {
    "sentiment": "Neutral",
    "confidence": 0.54
  },
  "meta": {
    "model": "TF-IDF + RandomForest",
    "version": "v1"
  }
}
```

---

## 🧪 Local Development

```bash
npm install
npm run dev
```

App runs at:
```
http://localhost:3000
```

---

## 🌐 Environment Variables

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Used to connect with the backend API.

---

## 🎯 Design Philosophy

- UI reflects model confidence visually
- Neutral predictions are clearly communicated
- Animations are subtle and meaningful
- No business logic duplication

---

## 🔮 Future Enhancements

- Improved accessibility
- Theme customization
- Mobile-focused UX refinements
