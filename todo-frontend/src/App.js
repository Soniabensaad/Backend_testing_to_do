import React, { useState } from "react";
import TodoList from "./TodoList";
import AddTodo from "./AddTodo";

const App = () => {
    const [todos, setTodos] = useState([]);

    const addTodo = (todo) => {
        setTodos([...todos, todo]);
    };

    return (
        <div>
            <h1>To-Do List</h1>
            <AddTodo onAdd={addTodo} />
            <TodoList todos={todos} />
        </div>
    );
};

export default App;
