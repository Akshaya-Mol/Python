import axios from "axios";
import { Link } from "react-router-dom";

function PostListItem(props) {
    function deletePost() {
        axios.delete('https://demo-blog.mashupstack.com/api/posts/'+props.post.id).then(response=>{
            alert(response.data.message)
            props.refresh()
        })
    }
    return <div className="card">
    <div className="card-body">
        {props.post.title}&nbsp;&nbsp;
        <button className="btn btn-primary float-right" onClick={deletePost}>Delete</button>&nbsp;&nbsp;
        <Link to={"/blog/posts/"+props.post.id+"/edit"} className="btn btn-primary float-right">Edit</Link>&nbsp;&nbsp;
        <Link to={"/blog/posts/"+props.post.id} className="btn btn-info float-right">View</Link>&nbsp;&nbsp;
    </div>
</div>
}
export default PostListItem;