import React, { useEffect, useState } from "react";
import api from './api';


const TodoList = () => {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        api.get("/todos").then((response) => {
            setTodos(response.data);
        });
    }, []);

    return (
        <ul>
            {todos.map((todo) => (
                <li key={todo.id}>{todo.title}</li>
            ))}
        </ul>
    );
};

export default TodoList;
