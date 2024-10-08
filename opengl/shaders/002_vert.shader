#version 330 core

layout (location=0) in vec3 vertexPos; 
layout (location=1) in vec3 vertexTexColor;
layout (location=2) in vec2 vertexTexCoord;

out vec3 fragmentTexColor;
out vec2 fragmentTexCoord;

void main(){

    gl_Position = vec4(vertexPos, 1.0);
    fragmentTexColor = vertexTexColor;
    fragmentTexCoord = vertexTexCoord;
}
