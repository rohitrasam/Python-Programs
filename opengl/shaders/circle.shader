#shader vertex
#version 330 core

layout (location=0) in vec3 pos;
layout (location=1) in vec3 color;

out vec3 colorCoord;

void main(){
    gl_Position = vec4(pos, 1.0);
    colorCoord = color;
}


// circle shape

#shader fragment
#version 330 core

in vec3 colorCoord;
out vec4 fragColor;

uniform float time;
uniform vec2 u_resolution;


float circle(vec2 position, float radius){
    return 1-step(radius, length(position-0.5));
}

vec2 randomVec(vec2 position){
    position += 0.05;
    float x = dot(position, vec2(987.654, 654.321));
    float y = dot(position, vec2(654.321, 765.432));
    vec2 randvec = vec2(x, y);
    randvec = sin(randvec)*2;
    randvec *= 42345.67890;
    randvec = sin(randvec+time);
    return randvec;
}

void main(){
    vec3 position = vec3(gl_FragCoord.xy / u_resolution, 1.0);
    // position = rotate() * (position-vec3(0.5));
    vec3 color = vec3(1.0);
    vec3 position1 = position;
    float rad = circle(position.xy, 0.4);
    position *= rad;
    position.xy *= 5;
    vec2 gridId = floor(position.xy);
    vec2 gridUv = fract(position.xy);

    // calculate the 4 corners of each cell
    vec2 bl = gridId + vec2(0.0, 0.0);
    vec2 br = gridId + vec2(1.0, 0.0);
    vec2 tl = gridId + vec2(0.0, 1.0);
    vec2 tr = gridId + vec2(1.0, 1.0);

    // generate random vectors on 4 corners of each cell
    vec2 randVecBl = randomVec(bl);
    vec2 randVecBr = randomVec(br);
    vec2 randVecTl = randomVec(tl);
    vec2 randVecTr = randomVec(tr);

    // calculate distance of 4 corners from each pixel
    vec2 distBl = gridUv - vec2(0.0);
    vec2 distBr = gridUv - vec2(1.0, 0.0);
    vec2 distTl = gridUv - vec2(0.0, 1.0);
    vec2 distTr = gridUv - vec2(1.0);

    // calculate teh dot product of random vectors and the vectors from 4 corners to each pixel
    float dotBl = dot(randVecBl, distBl);
    float dotBr = dot(randVecBr, distBr);
    float dotTl = dot(randVecTl, distTl);
    float dotTr = dot(randVecTr, distTr);

    // smoothen the grid patterns
    gridUv = smoothstep(0.2, 1.0, gridUv);
    // gridUv = step(0.4, gridUv);
    // gridUv = gridUv*gridUv*gridUv*(gridUv*(gridUv*6.0-15.0)+10.0);

    // interpolate the result
    float b = mix(dotBl, dotBr, gridUv.x);
    float t = mix(dotTl, dotTr, gridUv.x);
    float perlin = mix(b, t, gridUv.y);

    // perlin = smoothstep(0.0, 0.5, perlin);
    perlin = step(perlin, 0.01);
    color *= (0.1*perlin+0.1);
    float sky = circle(position1.xy, 0.35);
    color *= sky;
    

    fragColor = vec4(color*colorCoord, 1.0);
}

