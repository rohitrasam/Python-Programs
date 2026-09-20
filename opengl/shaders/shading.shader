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

vec3 palette(float t){
    vec3 a = vec3(0.5, 0.5, 0.5);
    vec3 b = vec3(0.5, 0.5, 0.5);
    vec3 c = vec3(1, 1, 1);
    vec3 d = vec3(0.263, 0.416, 0.557);
    return a * b*cos(6.2318*(c*t+d));
}

void main(){
    vec2 uv = gl_FragCoord.xy / u_resolution.xy;
    uv.x *= u_resolution.x/u_resolution.y;
    uv = uv*2 - 1;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0);
    for(int i=0; i < 2; i++){
        uv *= 2;
        uv = fract(uv);
        uv -= 0.5;
        float d = length(uv);
        vec3 col = palette(length(uv0)+time*0.5);
        d = sin(d*8+time)/8;
        d = abs(d);
        // d = smoothstep(0, 0.1, d);
        d = 0.02 / d;
        finalColor += col * d;
    }
    fragColor = vec4(finalColor, 1.0);

}