import axios from "axios";
import React from "react";
import BlogCard from "./BlogCard";

export default function Blog() {
  const [blogs, setBlogs] = React.useState([]);
  React.useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URI}/blog`)
      .then((resp) => {
        var data = resp.data;
        setBlogs([...data]);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const blogList = blogs.reverse().map((blog) => <BlogCard blog={blog} key={blog.id} />);

  return <div className="blog-container">{blogList}</div>;
}
