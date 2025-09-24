def isHappy(n):
  def get_next(number):
    total_sum = 0
    while number > 0:
      number, digit = divmod(number, 10)
      total_sum += digit ** 2
    return total_sum

  history = set()
  while n != 1 and n not in history:
    history.add(n)
    n = get_next(n)

  return n==1


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")

