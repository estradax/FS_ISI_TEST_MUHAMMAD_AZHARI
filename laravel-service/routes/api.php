<?php

use App\Http\Controllers\TodoListController;
use Illuminate\Support\Facades\Route;

Route::post('/v1/todos', [TodoListController::class, 'store']);
Route::put('/v1/todos/{id}', [TodoListController::class, 'update']);
Route::delete('/v1/todos/{id}', [TodoListController::class, 'destroy']);
