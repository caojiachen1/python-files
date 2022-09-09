#include<bits/stdc++.h>
#define eps 1e-21
using namespace std;
int p(int,int);
int p2(int,int,int);
int sprt(int,int,int);
int q(int);
bool isqrt(int k);
int a,b,c,delta;
int main()
{
	cout << "Input a:";
	cin >> a;
	cout << "Input b:";
	cin >> b;
	cout << "Input c:";
	cin >> c;
	if (a==0)
	{
		int xx=p(b,c);
		b/=xx;
		c/=xx;
		if (b!=1&&b!=0&&b!=-1)
		{
			if (c!=0) 
			{
				if (c<0)
				{
					cout << b << "x-" << -c <<"=0" << endl;
					if (c%b==0)
					{
						if (b>0) cout << "x=" << -c/b << endl;
				    	else if (b<0) cout << "x=-" << c/b << endl;
					}
					else 
					{
						if (b>0) cout << "x=" << -c << "/" << b << endl;
				    	else if (b<0) cout << "x=-" << -c << "/" << -b << endl;
					}
				}
				else
				{
					cout << b << "x+" << c <<"=0" << endl;
					if (c%b==0)
					{
						if (b>0) cout << "x=" << -c/b << endl;
			    		else if (b<0) cout << "x=-" << -c/b << endl;
					}
					else 
					{
						if (b>0) cout << "x=" << -c << "/" << b << endl;
				    	else if (b<0) cout << "x=-" << c << "/" << -b << endl;
					}
				}
			}
			else if (c==0) cout << "x=0" << endl; 
		}
		else if (b==1)
		{
			if (c!=0) 
			{
				if (c<0)
				{
					cout << "x-" << -c << "=0" << endl;
					cout << "x=" << -c << endl;
				}
				else 
				{
					cout << "x+" << c << "=0" << endl;
					cout << "x=" << -c << endl;
				}
			}
			else if (c==0) cout << "x=0" << endl; 
		}
		else if (b==0)
		{
			if (c!=0) 
			{
				cout << "No solution!" << endl;
				system("pause");
				return 0;
			}
			else if (c==0)
			{
				cout << "All x" << endl;
				system("pause");
				return 0;
			}
		}
		else if (b==-1)
		{
			if (c!=0) 
			{
				if (c<0)
				{
					cout << "-x-" << -c <<"=0" << endl;
					cout << "x=" << c << endl;
				}
				else 
				{
					cout << "-x+" << c <<"=0" << endl;
					cout << "x=" << c << endl;
				}
			}
			else if (c==0) cout << "x=0" << endl; 
		}
		system("pause");
		return 0;
	}
	int cj=p2(a,b,c);
	a/=cj;
	b/=cj;
	c/=cj;
	if (c==0)
	{
		if (a==1)
		{
			if (b==1) cout << "x^2+" << "x" << "=0" << endl; 
			else if (b==-1) cout << "x^2-" << "x" << "=0" << endl; 
			else 
			{
				if (b>0) cout << "x^2+" << b << "x" << "=0" << endl;
				else if (b<0) cout << "x^2-" << -b << "x" << "=0" << endl;
				else if (b==0) cout << "x^2" << "=0" << endl; 
			} 
		}
		else if (a==-1)
		{
			if (b==1) cout << "-x^2+" << "x" << "=0" << endl; 
			else if (b==-1) cout << "-x^2-" << "x" << "=0" << endl; 
			else 
			{
				if (b>0) cout << "-x^2+" << b << "x" << "=0" << endl;
				else if (b<0) cout << "-x^2-" << -b << "x" << "=0" << endl;
				else if (b==0) cout << "-x^2" << "=0" << endl; 
			} 
		}
		else 
		{
			if (b==1) cout << a << "x^2+" << "x" << "=0" << endl; 
			else if (b==-1) cout << a << "x^2-" << "x" << "=0" << endl; 
			else 
			{
				if (b>0) cout << a << "x^2+" << b << "x" << "=0" << endl; 
				else if (b<0) cout << a << "x^2-" << -b << "x" << "=0" << endl;
				else if (b==0) cout << a << "x^2" << "=0" << endl;
			}
		}
	}
	else 
	{
		if (c>0)
		{
			if (a==1)
			{
				if (b==1) cout << "x^2+" << "x+" << c << "=0" << endl; 
				else if (b==-1) cout << "x^2-" << "x+" << c << "=0" << endl; 
				else 
				{
					if (b>0) cout << "x^2+" << b << "x+" << c << "=0" << endl; 
					else if (b<0) cout << "x^2-" << -b << "x+" << c << "=0" << endl; 
					else if (b==0) cout << "x^2+" << c << "=0" << endl; 
				}
			}
			else if (a==-1)
			{
				if (b==1) cout << "-x^2+" << "x+" << c << "=0" << endl; 
				else if (b==-1) cout << "-x^2-" << "x+" << c << "=0" << endl; 
				else 
				{
					if (b>0) cout << "-x^2+" << b << "x+" << c << "=0" << endl; 
					else if (b<0) cout << "-x^2-" << -b << "x+" << c << "=0" << endl; 
					else if (b==0) cout << "-x^2+" << c << "=0" << endl; 
				}
			}
			else 
			{
				if (b==1) cout << a << "x^2+" << "x+" << c << "=0" << endl; 
				else if (b==-1) cout << a << "x^2-" << "x+" << c << "=0" << endl; 
				else 
				{
					if (b>0) cout << a << "x^2+" << b << "x+" << c << "=0" << endl; 
					else if (b<0) cout << a << "x^2-" << -b << "x+" << c << "=0" << endl; 
					else if (b==0) cout << a << "x^2+" << c << "=0" << endl; 
				}
			}
		}
		else if (c<0)
		{
			if (a==1)
			{
				if (b==1) cout << "x^2+" << "x-" << -c << "=0" << endl; 
				else if (b==-1) cout << "x^2-" << "x-" << -c << "=0" << endl; 
				else 
				{
					if (b>0) cout << "x^2+" << b << "x-" << -c << "=0" << endl; 
					else if (b<0) cout << "x^2-" << -b << "x-" << -c << "=0" << endl; 
					else if (b==0) cout << "x^2-" << -c << "=0" << endl; 
				}
			}
			else if (a==-1)
			{
				if (b==1) cout << "-x^2+" << "x-" << -c << "=0" << endl; 
				else if (b==-1) cout << "-x^2-" << "x-" << -c << "=0" << endl; 
				else 
				{
					if (b>0) cout << "-x^2+" << b << "x-" << -c << "=0" << endl; 
					else if (b<0) cout << "-x^2-" << -b << "x-" << -c << "=0" << endl; 
					else if (b==0) cout << "-x^2-" << -c << "=0" << endl; 
				}
			}
			else 
			{
				if (b==1) cout << a << "x^2+" << "x-" << -c << "=0" << endl; 
				else if (b==-1) cout << a << "x^2-" << "x-" << -c << "=0" << endl; 
				else 
				{
					if (b>0) cout << a << "x^2+" << b << "x-" << -c << "=0" << endl; 
					else if (b<0) cout << a << "x^2-" << -b << "x-" << -c << "=0" << endl; 
					else if (b==0) cout << a << "x^2-" << -c << "=0" << endl; 
				}
			}
		}
	}
	int de=2*a;
	delta=b*b-4*a*c;
	cout << "Delta=" << delta << endl;
	if (delta<0)
	{
		cout << "Unreal solution" << endl;
		delta=-delta;
		if (isqrt(delta))
		{
			delta=(int)(sqrt(delta));
			int a0,b0;
			int aa=p2(b,delta,de);
			b/=aa;
			delta/=aa;
			de/=aa;
			if (b==0)
			{
				if (de==1)
		    	{
		    		if (delta==1)
		    		{
		    			cout << "x1=" << "i" << endl;
	                	cout << "x2=" << "-i" << endl;
	    			}
		    		else
	    			{
	    				cout << "x1=" << delta << "i" << endl;
	                	cout << "x2=" << "-" << delta << "i" << endl;
	    			}
		    	}
		    	else if (de==-1)
		    	{
		    		if (delta==1)
		    		{
		    			cout << "x1=" << "i" << endl;
	                	cout << "x2=" << "-i" << endl;
	    			}
		    		else
	    			{
	    				cout << "x1=" << delta << "i" << endl;
	                	cout << "x2=" << "-" << delta << "i" << endl;
	    			}
		    	}
	    		else
	    		{
		    		if (delta==1)
		    		{
		    			cout << "x1=(" << -b << "+" << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << "i)/" << de << endl;
		    		}
		    		else
		    		{
		    			cout << "x1=(" << -b << "+" << delta << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << delta << "i)/" << de << endl;
		    		}
		    	}
			}
			else if (b>0)
			{
				if (de==1)
		    	{
	    			if (delta==1)
	    			{
	    				cout << "x1=" << -b << "+" << "i" << endl;
	                	cout << "x2=" << -b << "-" << "i" << endl;
	    			}
	    			else
	    			{
	    				cout << "x1=" << -b << "+" << delta << "i" << endl;
	                	cout << "x2=" << -b << "-" << delta << "i" << endl;
		    		}
	    		}
	    		else if (de==-1)
	    		{
	    			if (delta==1)
	    			{
	    				cout << "x1=" << -b << "+" << "i" << endl;
	                	cout << "x2=" << -b << "-" << "i" << endl;
	    			}
	    			else
	    			{
	    				cout << "x1=" << b << "+" << delta << "i" << endl;
	                	cout << "x2=" << b << "-" << delta << "i" << endl;
		    		}
	    		}
	    		else
	    		{
	    			if (delta==1)
	    			{
	    				cout << "x1=(" << -b << "+" << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << "i)/" << de << endl;
	    			}
	    			else
		    		{
	     				cout << "x1=(" << -b << "+" << delta << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << delta << "i)/" << de << endl;
	    			}
	    		}
			}
			else if (b<0)
			{
				if (de==1)
		    	{
	    			if (delta==1)
	    			{
	    				cout << "x1=" << -b << "+" << "i" << endl;
	                	cout << "x2=" << -b << "-" << "i" << endl;
	    			}
	    			else
	    			{
	    				cout << "x1=" << -b << "+" << delta << "i" << endl;
	                	cout << "x2=" << -b << "-" << delta << "i" << endl;
		    		}
	    		}
	    		else if (de==-1)
	    		{
	    			if (delta==1)
	    			{
	    				cout << "x1=-" << -b << "+" << "i" << endl;
	                	cout << "x2=-" << -b << "-" << "i" << endl;
	    			}
	    			else
	    			{
	    				cout << "x1=-" << -b << "+" << delta << "i" << endl;
	                	cout << "x2=-" << -b << "-" << delta << "i" << endl;
		    		}
	    		}
	    		else
	    		{
	    			if (delta==1)
	    			{
	    				cout << "x1=(" << -b << "+" << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << "i)/" << de << endl;
	    			}
	    			else
		    		{
	     				cout << "x1=(" << -b << "+" << delta << "i)/" << de << endl;
	                    cout << "x2=(" << -b << "-" << delta << "i)/" << de << endl;
	    			}
	    		}
			}
		}
		else
		{
			int aa=sprt(b,delta,de);
			b/=aa;
			delta/=aa*aa;
			de/=aa;
			int aaa=q(delta);
			if (b==0)
			{
				if (de==1)
				{
					if (aaa==1)
					{
						cout << "x1=" << "sqrt(" << delta << ")i" << endl;
	      		  	    cout << "x2=" << "-sqrt(" << delta << ")i" << endl;
					}
					else
					{
						cout << "x1=" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	        		    cout << "x2=" << -aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
					}
				}
				else if (de==-1)
				{
					if (aaa==1)
					{
						cout << "x1=" << "sqrt(" << delta << ")i" << endl;
	      		  	    cout << "x2=" << "-sqrt(" << delta << ")i" << endl;
					}
					else if (aaa>0)
					{
						cout << "x1=-" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	        		    cout << "x2=-" << -aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
					}
					else
					{
						cout << "x1=" << -aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	        		    cout << "x2=-" << -aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
					}
				}
				else
				{
					if (aaa==1)
					{
						cout << "x1=(" << "sqrt(" << delta << ")i)/" << de << endl;
	       		     	cout << "x2=(" << "-sqrt(" << delta << ")i)/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
	       		     	cout << "x2=(" << -aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
					}
				}
			}
			else if (b>0)
			{
				if (de==1)
		    	{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << -b << "+sqrt(" << delta << ")i" << endl;
	            	    cout << "x2=" << -b << "-sqrt(" << delta << ")i" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	            	    cout << "x2=" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	    			}
	    		}
	    		else if (de==-1)
	    		{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << b << "+sqrt(" << delta << ")i" << endl;
	            	    cout << "x2=" << b << "-sqrt(" << delta << ")i" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	            	    cout << "x2=" << b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	    			}
	    		}
	    		else
	    		{
	    			if (aaa==1)
	    			{
	    				cout << "x1=(" << -b << "+sqrt(" << delta << ")i)/" << de << endl;
	                	cout << "x2=(" << -b << "-sqrt(" << delta << ")i)/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
	     		       	cout << "x2=(" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
					}
				}
			}
			else if (b<0)
			{
				if (de==1)
		    	{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << -b << "+sqrt(" << delta << ")i" << endl;
	            	    cout << "x2=" << -b << "-sqrt(" << delta << ")i" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	            	    cout << "x2=" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	    			}
	    		}
	    		else if (de==-1)
	    		{
	    			if (aaa==1)
		    		{
		    			cout << "x1=-" << -b << "+sqrt(" << delta << ")i" << endl;
	            	    cout << "x2=-" << -b << "-sqrt(" << delta << ")i" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=-" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	            	    cout << "x2=-" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i" << endl;
	    			}
	    		}
	    		else
	    		{
	    			if (aaa==1)
	    			{
	    				cout << "x1=(" << -b << "+sqrt(" << delta << ")i)/" << de << endl;
	                	cout << "x2=(" << -b << "-sqrt(" << delta << ")i)/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
	     		       	cout << "x2=(" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")i)/" << de << endl;
					}
				}
			}
		}
		system("pause");
		return 0;
	}
	else 
	{
		cout << "Real solution"  << endl;
		if (isqrt(delta))
		{
			delta=(int)(sqrt(delta));
			int a0,b0;
			a0=delta-b;
			b0=-b-delta;
			double g,h;
			g=a0/de;
			h=b0/de;
			if (abs(a0-b0)<=1e-200) 
			{
				cout << "x1=x2=" << g << endl;
				system("pause");
				return 0;
			}
			if (a0==0) cout << "x1=0" << endl;
			else if (a0%de==0) cout << "x1=" << g << endl;
			else 
			{
				if (g>0) cout << "x1=" << abs(a0/p(a0,de)) << "/" << abs(de/p(a0,de)) << endl;
				else cout << "x1=-" << abs(a0/p(a0,de)) << "/" << abs(de/p(a0,de)) << endl;
			}
			if (b0==0) cout << "x2=0" << endl;
			else if (b0%de==0) cout << "x2=" << h << endl;
			else 
			{
				if (h>0) cout << "x2=" << abs(b0/p(b0,de)) << "/" << abs(de/p(b0,de)) << endl;
				else cout << "x2=-" << abs(b0/p(b0,de)) << "/" << abs(de/p(b0,de)) << endl;
			}
		}
		else
		{
			int aa=sprt(b,delta,de);
			b/=aa;
			delta/=aa*aa;
			de/=aa;
			int aaa=q(delta);
			if (b==0)
			{
				if (de==1)
				{
					if (aaa==1)
					{
						cout << "x1=" << "sqrt(" << delta << ")" << endl;
	      		  	    cout << "x2=" << "-sqrt(" << delta << ")" << endl;
					}
					else
					{
						cout << "x1=" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	        		    cout << "x2=" << -aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
					}
				}
				else if (de==-1)
				{
					if (aaa==1)
					{
						cout << "x1=" << "sqrt(" << delta << ")" << endl;
	      		  	    cout << "x2=" << "-sqrt(" << delta << ")" << endl;
					}
					else if (aaa>0)
					{
						cout << "x1=" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	        		    cout << "x2=" << -aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
					}
					else if (aaa<0)
					{
						cout << "x1=" << -aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	        		    cout << "x2=-" << -aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
					}
				}
				else
				{
					if (aaa==1)
					{
						cout << "x1=(" << "sqrt(" << delta << "))/" << de << endl;
	       		     	cout << "x2=(" << "-sqrt(" << delta << "))/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
	       		     	cout << "x2=(" << -aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
					}
				}
			}
			else if (b>0)
			{
				if (de==1)
		    	{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << -b << "+sqrt(" << delta << ")" << endl;
	            	    cout << "x2=" << -b << "-sqrt(" << delta << ")" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	            	    cout << "x2=" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	    			}
	    		}
	    		else if (de==-1)
	    		{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << b << "+sqrt(" << delta << ")" << endl;
	            	    cout << "x2=" << -b << "-sqrt(" << delta << ")" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	            	    cout << "x2=" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	    			}
	    		}
	    		else
	    		{
	    			if (aaa==1)
	    			{
	    				cout << "x1=(" << -b << "+sqrt(" << delta << "))/" << de << endl;
	                	cout << "x2=(" << -b << "-sqrt(" << delta << "))/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
	     		       	cout << "x2=(" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
					}
				}
			}
			else if (b<0)
			{
				if (de==1)
		    	{
	    			if (aaa==1)
		    		{
		    			cout << "x1=" << -b << "+sqrt(" << delta << ")" << endl;
	            	    cout << "x2=" << -b << "-sqrt(" << delta << ")" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	            	    cout << "x2=" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	    			}
	    		}
	    		else if (de==-1)
	    		{
	    			if (aaa==1)
		    		{
		    			cout << "x1=-" << -b << "+sqrt(" << delta << ")" << endl;
	            	    cout << "x2=-" << -b << "-sqrt(" << delta << ")" << endl;
	    			}
		    		else
		    		{
		    			cout << "x1=-" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	            	    cout << "x2=-" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << ")" << endl;
	    			}
	    		}
	    		else
	    		{
	    			if (aaa==1)
	    			{
	    				cout << "x1=(" << -b << "+sqrt(" << delta << "))/" << de << endl;
	                	cout << "x2=(" << -b << "-sqrt(" << delta << "))/" << de << endl;
					}
					else
					{
					    cout << "x1=(" << -b << "+" << aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
	     		       	cout << "x2=(" << -b << "-" << aaa << "sqrt(" << delta/aaa/aaa << "))/" << de << endl;
					}
				}
			}
		}
		system("pause");
		return 0;
	}
}
int p(int k,int o)
{
	for (int i=max(abs(k),abs(o));i>=1;--i) if (abs(k)%i==0&&abs(o)%i==0) return i;
	return 1;
}
int p2(int k,int o,int j)
{
	for (int i=max(k,max(o,j));i>=1;--i) if (k%i==0&&o%i==0&&j%i==0) return i;
	return 1;
}
int sprt(int k,int o,int j)
{
	for (int i=max(k,max(o,j));i>=1;--i) if (k%i==0&&o%(i*i)==0&&j%i==0) return i;
	return 1;
}
int q(int k)
{
	for (int i=k;i>=1;--i) if (k%(i*i)==0) return i;
	return 1;
}
bool isqrt(int k)
{
	for (int i=0;i<=k;++i) if (i*i==k) return true;
	return false;
}