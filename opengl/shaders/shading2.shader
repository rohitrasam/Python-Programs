#shader vertex
#version 330 core

layout (location=0) in vec3 pos;
layout (location=1) in vec3 color;

out vec3 colorCoord;

void main(){
    gl_Position = vec4(pos, 1.0);
    colorCoord = color;
}

#shader fragment
#version 330 core

in vec3 colorCoord;
out vec4 fragColor;

uniform float time;
uniform vec2 u_resolution;

void main(){

    vec2 uv = gl_FragCoord.xy / u_resolution;
    uv = uv*2 - 1;
    uv.x = abs(sin(uv.x*uv.y+time));
    float d = length(uv);
    d = step(0.1, d);
    fragColor = vec4(uv.x, d, d, 1.0);


}