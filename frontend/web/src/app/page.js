"use client";

import { useState } from "react";

export default function Home() {
  const [result, setResult] = useState(null);

  return (
    <main className="min-h-screen bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 flex items-center justify-center px-4">
      
      <div className="w-full max-w-lg bg-white/90 dark:bg-neutral-900/90 backdrop-blur-xl 
                      rounded-3xl shadow-2xl p-8 border border-white/20">
        
        {/* Header */}
        <h1 className="text-3xl font-extrabold text-center tracking-tight text-gray-800 dark:text-white">
          Sentiment Analyzer
        </h1>
        <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-1">
          Feel the emotion behind words ✨
        </p>

        {/* Input */}
        <div className="mt-8">
          <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">
            Your text
          </label>
          <textarea
            placeholder="Example: I absolutely loved the experience!"
            className="w-full h-32 p-4 rounded-2xl border border-gray-300 dark:border-neutral-700 
                       bg-white dark:bg-neutral-800 text-gray-800 dark:text-white
                       focus:outline-none focus:ring-4 focus:ring-purple-500/40 
                       resize-none transition"
          />
        </div>

        {/* Button */}
        <button
          onClick={() => setResult("Positive")}
          className="w-full mt-8 py-3 rounded-2xl font-semibold text-white text-lg
                     bg-gradient-to-r from-purple-600 to-pink-600
                     hover:shadow-xl hover:scale-[1.02]
                     active:scale-[0.97]
                     transition-all duration-200"
        >
          Analyze Sentiment 🚀
        </button>

        {/* Result */}
        <div className="mt-8 text-center">
          <p className="text-sm uppercase tracking-wide text-gray-500 dark:text-gray-400">
            Result
          </p>

          <div
            className={`mt-3 inline-flex items-center gap-2 px-6 py-3 rounded-full text-lg font-bold
              ${
                result === "Positive"
                  ? "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400"
                  : "bg-gray-100 text-gray-600 dark:bg-neutral-800 dark:text-gray-300"
              }`}
          >
            {result === "Positive" ? "😊 Positive" : "—"}
          </div>
        </div>

      </div>
    </main>
  );
}
