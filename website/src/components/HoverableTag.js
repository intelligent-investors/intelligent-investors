import React, { useState } from 'react';
import { Tag } from 'antd';

function HoverableTag({ content, url }) {
  const [hover, setHover] = useState(false);

  const TagContent = (
    <Tag
      color={hover ? "rgba(0, 0, 0, 0.88)" : false}
      style={{
        marginTop: 12,
        cursor: 'pointer',
        transition: 'color 0.3s'
      }}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
    >
      {content}
    </Tag>
  );

  // Conditionally render the <a> tag if a URL is provided
  return url ? (
    <a href={url} target="_blank" rel="noopener noreferrer">
      {TagContent}
    </a>
  ) : TagContent;
}

export default HoverableTag;
