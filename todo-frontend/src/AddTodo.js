import React, { useState } from "react";
import api from './api';


const AddTodo = ({ onAdd }) => {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newTodo = { title, description, completed: false };
        const response = await api.post("/todos", newTodo);
        onAdd(response.data);
        setTitle("");
        setDescription("");
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button type="submit">Add</button>
        </form>
    );
};

export default AddTodo;
