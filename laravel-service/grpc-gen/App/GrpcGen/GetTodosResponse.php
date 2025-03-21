<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: todo.proto

namespace App\GrpcGen;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>GetTodosResponse</code>
 */
class GetTodosResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>repeated .TodoMessage todos = 1;</code>
     */
    private $todos;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type array<\App\GrpcGen\TodoMessage>|\Google\Protobuf\Internal\RepeatedField $todos
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Todo::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>repeated .TodoMessage todos = 1;</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getTodos()
    {
        return $this->todos;
    }

    /**
     * Generated from protobuf field <code>repeated .TodoMessage todos = 1;</code>
     * @param array<\App\GrpcGen\TodoMessage>|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setTodos($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \App\GrpcGen\TodoMessage::class);
        $this->todos = $arr;

        return $this;
    }

}

