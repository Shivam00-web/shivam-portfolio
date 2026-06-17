import { useState } from 'react';

export default function DisplayImage({ src, alt, className, placeholder = '◆' }) {
  const [failed, setFailed] = useState(false);

  if (!src || failed) {
    return <span className={className}>{placeholder}</span>;
  }

  return (
    <img
      src={src}
      alt={alt}
      className={className}
      onError={() => setFailed(true)}
    />
  );
}
