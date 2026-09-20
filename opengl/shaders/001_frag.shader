#version 330 core

in vec3 fragmentTexColor;

out vec4 color;

void main(){
    color = vec4(fragmentTexColor, 1.0);
}