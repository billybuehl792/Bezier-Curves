function easeCustom(t,tMin,tMax,val1,val2){
	z=arguments;
	if(z.length!==5) return value;
	a=z[4]-z[3];
	b=z[2]-z[1];
	c=clamp((z[0]-z[1])/(b/2), 0, 2);
	if(c<1) return a/2*Math.pow(c,5)+z[3];
	c-=2;
	return a/2*(Math.pow(c,5)+2)+z[3];
};
