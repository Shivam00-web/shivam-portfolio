const API_BASE = import.meta.env.VITE_API_URL || 'https://shivam-portfolio-ad8n.onrender.com/api'; 

export async function fetchPortfolio() {
  const res = await fetch(`${API_BASE}/portfolio/`);
  if (!res.ok) throw new Error('Failed to fetch portfolio data');
  return res.json();
}

export async function submitContact(data) {
  const res = await fetch(`${API_BASE}/contact/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Failed to send message');
  }
  return res.json();
}
