class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        ans = []
        ans.append(Kelvin)
        ans.append(Fahrenheit)
        return(ans)
Output = Solution().convertTemperature(celsius = 36.50)
print(Output)