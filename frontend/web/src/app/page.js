"use client";

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [confidence, setConfidence] = useState(null);

  async function analyzeSentiment() {
    if (!text.trim()) return;

    setLoading(true);
    setResult(null);
    setConfidence(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/sentiment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await res.json();
      setResult(data.sentiment);
      setConfidence(data.confidence);
    } catch (e) {
      setResult("Error");
    } finally {
      setLoading(false);
    }
  }

  const sentimentMap = {
    Positive: { emoji: "😊", label: "Positive mood" },
    Negative: { emoji: "😡", label: "Negative mood" },
    Neutral: { emoji: "😐", label: "Neutral mood" },
    Error: { emoji: "⚠️", label: "Error" },
  };

  const meta = sentimentMap[result];

  /* 🎨 CONFIDENCE → GRADIENT COLOR */
  function confidenceGradient(conf) {
    if (conf >= 0.8)
      return "from-emerald-400 via-green-500 to-emerald-600";
    if (conf >= 0.6)
      return "from-sky-400 via-blue-500 to-indigo-600";
    return "from-yellow-300 via-amber-400 to-orange-400";
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 flex items-center justify-center px-4">
      <div className="w-full max-w-xl bg-white/90 backdrop-blur-2xl rounded-3xl shadow-[0_20px_60px_rgba(0,0,0,0.25)] p-8">

        {/* Header */}
        <h1 className="text-4xl font-extrabold text-center text-gray-900 tracking-tight">
          Sentiment Analyzer
        </h1>
        <p className="text-center text-sm text-gray-500 mt-2">
          AI that understands emotions behind text
        </p>

        {/* Input */}
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type something like: I am feeling okay today..."
          className="w-full h-32 mt-8 p-4 rounded-2xl border border-gray-300
                     focus:outline-none focus:ring-4 focus:ring-purple-300
                     resize-none text-gray-800"
        />

        {/* Button */}
        <button
          onClick={analyzeSentiment}
          disabled={loading}
          className="w-full mt-6 py-3 rounded-2xl text-white font-semibold text-lg
                     bg-gradient-to-r from-purple-600 to-pink-600
                     hover:scale-[1.04] transition-transform
                     disabled:opacity-60"
        >
          {loading ? "Analyzing sentiment..." : "Analyze Sentiment"}
        </button>

        {/* Result Card */}
        {meta && (
          <div className="mt-10 rounded-2xl p-6 bg-white shadow-inner border border-gray-200">

            <div className="flex items-center justify-center gap-3 text-2xl font-bold mb-4">
              <span>{meta.emoji}</span>
              <span className="text-gray-800">{meta.label}</span>
            </div>

            {/* 🌈 BEAUTIFUL CONFIDENCE BAR */}
            {confidence !== null && (
              <div className="mt-4">
                <div className="flex justify-between text-sm text-gray-600 mb-2">
                  <span>Confidence</span>
                  <span className="font-semibold">
                    {(confidence * 100).toFixed(1)}%
                  </span>
                </div>

                <div className="relative w-full h-4 bg-gray-200 rounded-full overflow-hidden">
                  <div
                    className={`absolute inset-y-0 left-0 rounded-full 
                                bg-gradient-to-r ${confidenceGradient(confidence)}
                                transition-all duration-1000 ease-out`}
                    style={{ width: `${confidence * 100}%` }}
                  />
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </main>
  );
}
