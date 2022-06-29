import React from "react";

export default function BlogCard({ blog }) {
  const [show, setShow] = React.useState(false);
  const [blogBody, setBlogBody] = React.useState(
    blog.body
  );
  React.useEffect(() => {
    if (!show) {
      if (blog.body.length > 100) {
        setBlogBody(blog.body.substring(0, 100) + "...");
      }
    } else {
      setBlogBody(blog.body);
    }
  }, [blog.body, show]);
  return (
    <div className="blog-card-container" onClick={() => setShow(!show)}>
      <h1>{blog.title}</h1>
      <p style={{textAlign: 'left'}}>{blogBody}</p>
    </div>
  );
}
