#version 330 core

in vec3 fragmentTexColor;
in vec2 fragmentTexCoord;

out vec4 color;
uniform sampler2D imageTexture;

void main(){
    color = vec4(fragmentTexColor, 1.0) * texture(imageTexture, fragmentTexCoord);
}