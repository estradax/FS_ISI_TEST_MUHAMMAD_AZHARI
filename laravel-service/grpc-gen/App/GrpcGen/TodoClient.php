<?php
// GENERATED CODE -- DO NOT EDIT!

namespace App\GrpcGen;

/**
 */
class TodoClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * @param \App\GrpcGen\GetTodosRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function GetTodos(\App\GrpcGen\GetTodosRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/Todo/GetTodos',
        $argument,
        ['\App\GrpcGen\GetTodosResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \App\GrpcGen\CreateTodoRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function CreateTodo(\App\GrpcGen\CreateTodoRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/Todo/CreateTodo',
        $argument,
        ['\App\GrpcGen\CreateTodoResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \App\GrpcGen\UpdateTodoRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function UpdateTodo(\App\GrpcGen\UpdateTodoRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/Todo/UpdateTodo',
        $argument,
        ['\App\GrpcGen\UpdateTodoResponse', 'decode'],
        $metadata, $options);
    }

    /**
     * @param \App\GrpcGen\DeleteTodoRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function DeleteTodo(\App\GrpcGen\DeleteTodoRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/Todo/DeleteTodo',
        $argument,
        ['\App\GrpcGen\DeleteTodoResponse', 'decode'],
        $metadata, $options);
    }

}
