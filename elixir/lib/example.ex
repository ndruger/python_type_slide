defmodule Example do
  @spec f1(String.t) :: :ok
  defp f1(a) do
    IO.puts(a)
  end

  defp f2(a) do
    f1(a)
  end

  def main() do
    f2(10) # エラー。
    # f2("text") # OK
  end
end
