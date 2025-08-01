import React, { useState } from "react";

// Enhanced polka dots pattern with subtle glow
const polkaDotsBackground = `
  radial-gradient(circle at 25% 25%, rgba(139, 92, 246, 0.12) 2px, transparent 2px),
  radial-gradient(circle at 75% 75%, rgba(236, 72, 153, 0.08) 2px, transparent 2px),
  radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.06) 1px, transparent 1px),
  linear-gradient(135deg, rgba(139, 92, 246, 0.02) 0%, rgba(236, 72, 153, 0.02) 100%)
`;

// Loader component
const Loader = () => (
  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
    <div
      style={{
        width: '20px',
        height: '20px',
        borderRadius: '50%',
        background: 'conic-gradient(from 0deg, transparent, #8b5cf6, transparent)',
        animation: 'spin 1s linear infinite',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}
    >
      <div
        style={{
          width: '14px',
          height: '14px',
          borderRadius: '50%',
          backgroundColor: '#1a1a1a'
        }}
      />
    </div>
    <span style={{ fontSize: '18px', fontFamily: "'IBM Plex Sans', 'Inter', sans-serif", fontWeight: '500', letterSpacing: '0.01em' }}>Searching...</span>
    <style jsx>{`
      @keyframes spin {
        to { transform: rotate(360deg); }
      }
    `}</style>
  </div>
);

function App() {
  const [query, setQuery] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSummary("");
    setError("");
    if (!query.trim()) return;

    setLoading(true);
    try {
      const response = await fetch("/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.detail || "API error");
      } else {
        const data = await response.json();
        setSummary(data.summary);
      }
    } catch {
      setError("Network error");
    }
    setLoading(false);
  };

  return (
    <>
      <style>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
        
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes glow {
          0%, 100% { box-shadow: 0 0 20px rgba(139, 92, 246, 0.3); }
          50% { box-shadow: 0 0 30px rgba(139, 92, 246, 0.5); }
        }
        
        .fade-in {
          animation: fadeIn 0.5s ease-out;
        }
        
        .glow-effect:focus {
          animation: glow 2s ease-in-out infinite;
        }
      `}</style>

      <div
        style={{
          minHeight: "100vh",
          backgroundColor: "#0a0a0a",
          backgroundImage: polkaDotsBackground,
          backgroundPosition: "0 0, 15px 15px, 7px 7px, 0 0",
          backgroundSize: "30px 30px, 30px 30px, 15px 15px, 100% 100%",
          color: "#f1f5f9",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          padding: "20px",
          fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
          position: "relative",
          overflow: "hidden"
        }}
      >
        {/* Ambient light effect */}
        <div
          style={{
            position: "absolute",
            top: "20%",
            left: "10%",
            width: "200px",
            height: "200px",
            background: "radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%)",
            borderRadius: "50%",
            filter: "blur(60px)",
            animation: "glow 4s ease-in-out infinite alternate"
          }}
        />

        <div
          style={{
            position: "absolute",
            bottom: "30%",
            right: "15%",
            width: "150px",
            height: "150px",
            background: "radial-gradient(circle, rgba(236, 72, 153, 0.08) 0%, transparent 70%)",
            borderRadius: "50%",
            filter: "blur(50px)",
            animation: "glow 3s ease-in-out infinite alternate-reverse"
          }}
        />

        <div
          style={{
            maxWidth: "680px",
            width: "100%",
            borderRadius: "24px",
            boxShadow: `
              0 25px 50px rgba(0, 0, 0, 0.8),
              0 0 0 1px rgba(255, 255, 255, 0.05),
              inset 0 1px 0 rgba(255, 255, 255, 0.1)
            `,
            padding: "40px",
            backdropFilter: "blur(20px)",
            border: "1px solid rgba(139, 92, 246, 0.2)",
            position: "relative",
            zIndex: 1
          }}
        >
          {/* Header with gradient text */}
          <div style={{ textAlign: "center", marginBottom: "32px" }}>
            <h1
              style={{
                fontSize: "38px",
                fontWeight: "700",
                background: "linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #3b82f6 100%)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
                backgroundClip: "text",
                marginBottom: "8px",
                letterSpacing: "0.02em",
                fontFamily: "'IBM Plex Sans', 'Inter', sans-serif"
              }}
            >
              Ripplica Query Agent
            </h1>
            <p
              style={{
                color: "#94a3b8",
                fontSize: "18px",
                margin: 0,
                fontWeight: "400",
                letterSpacing: "0.01em",
                fontFamily: "'IBM Plex Sans', 'Inter', sans-serif"
              }}
            >
              Intelligent search powered by AI
            </p>
          </div>

          <div style={{ marginBottom: "24px" }}>
            <div style={{ position: "relative", marginBottom: "20px" }}>
              <input
                type="text"
                placeholder="Ask me anything..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="glow-effect"
                style={{
                  width: "100%",
                  padding: "20px 24px",
                  fontSize: "18px",
                  borderRadius: "16px",
                  border: "2px solid rgba(75, 85, 99, 0.3)",
                  backgroundColor: "rgba(30, 30, 30, 0.8)",
                  color: "#f1f5f9",
                  outline: "none",
                  transition: "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                  fontFamily: "'IBM Plex Sans', 'Inter', sans-serif",
                  boxSizing: "border-box",
                  letterSpacing: "0.01em",
                  fontWeight: "500"
                }}
                onFocus={(e) => {
                  e.target.style.borderColor = "#8b5cf6";
                  e.target.style.backgroundColor = "rgba(30, 30, 30, 1)";
                  e.target.style.transform = "translateY(-2px)";
                }}
                onBlur={(e) => {
                  e.target.style.borderColor = "rgba(75, 85, 99, 0.3)";
                  e.target.style.backgroundColor = "rgba(30, 30, 30, 0.8)";
                  e.target.style.transform = "translateY(0)";
                }}
              />

              {/* Search icon */}
              <div
                style={{
                  position: "absolute",
                  right: "20px",
                  top: "50%",
                  transform: "translateY(-50%)",
                  color: "#64748b",
                  pointerEvents: "none"
                }}
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21.71 20.29L18 16.61A9 9 0 1 0 16.61 18L20.29 21.71A1 1 0 0 0 21.71 20.29ZM11 18A7 7 0 1 1 18 11A7 7 0 0 1 11 18Z" />
                </svg>
              </div>
            </div>

            <button
              onClick={handleSubmit}
              disabled={loading || !query.trim()}
              style={{
                width: "100%",
                padding: "20px 24px",
                borderRadius: "16px",
                border: "none",
                background: loading || !query.trim()
                  ? "rgba(75, 85, 99, 0.5)"
                  : "linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)",
                color: "white",
                fontWeight: "600",
                fontSize: "18px",
                cursor: loading || !query.trim() ? "not-allowed" : "pointer",
                boxShadow: loading || !query.trim()
                  ? "none"
                  : "0 8px 25px rgba(139, 92, 246, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1)",
                transition: "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                fontFamily: "'IBM Plex Sans', 'Inter', sans-serif",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                minHeight: "56px",
                letterSpacing: "0.02em"
              }}
              onMouseEnter={(e) => {
                if (!loading && query.trim()) {
                  e.target.style.transform = "translateY(-2px)";
                  e.target.style.boxShadow = "0 12px 35px rgba(139, 92, 246, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.1)";
                }
              }}
              onMouseLeave={(e) => {
                if (!loading && query.trim()) {
                  e.target.style.transform = "translateY(0)";
                  e.target.style.boxShadow = "0 8px 25px rgba(139, 92, 246, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1)";
                }
              }}
            >
              {loading ? <Loader /> : "Search"}
            </button>
          </div>

          {error && (
            <div
              className="fade-in"
              style={{
                padding: "16px 20px",
                backgroundColor: "rgba(239, 68, 68, 0.1)",
                border: "1px solid rgba(239, 68, 68, 0.3)",
                borderRadius: "12px",
                color: "#fca5a5",
                fontWeight: "500",
                textAlign: "center",
                marginBottom: "20px",
                fontSize: "18px",
                fontFamily: "'IBM Plex Sans', 'Inter', sans-serif",
                letterSpacing: "0.01em"
              }}
            >
              <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "8px" }}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 2A10 10 0 1 0 22 12A10 10 0 0 0 12 2ZM12 17A1.5 1.5 0 1 1 13.5 15.5A1.5 1.5 0 0 1 12 17ZM12 13A1 1 0 0 1-1-1V8A1 1 0 0 1 2 0Z" />
                </svg>
                {error}
              </div>
            </div>
          )}

          {summary && (
            <div
              className="fade-in"
              style={{
                backgroundColor: "rgba(30, 41, 59, 0.6)",
                border: "1px solid rgba(71, 85, 105, 0.3)",
                padding: "24px",
                borderRadius: "16px",
                lineHeight: "1.7",
                boxShadow: "inset 0 1px 0 rgba(255, 255, 255, 0.05)"
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: "12px", marginBottom: "16px" }}>
                <div
                  style={{
                    width: "8px",
                    height: "8px",
                    borderRadius: "50%",
                    background: "linear-gradient(135deg, #8b5cf6, #ec4899)",
                    boxShadow: "0 0 10px rgba(139, 92, 246, 0.6)"
                  }}
                />
                <h2
                  style={{
                    margin: 0,
                    fontSize: "20px",
                    fontWeight: "600",
                    color: "#e2e8f0",
                    fontFamily: "'IBM Plex Sans', 'Inter', sans-serif",
                    letterSpacing: "0.01em"
                  }}
                >
                  Summary
                </h2>
              </div>
              <div
                style={{
                  color: "#cbd5e1",
                  fontSize: "17px",
                  whiteSpace: "pre-wrap",
                  lineHeight: "1.6",
                  fontFamily: "'IBM Plex Sans', 'Inter', sans-serif",
                  letterSpacing: "0.01em",
                  fontWeight: "400"
                }}
              >
                {summary}
              </div>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default App;