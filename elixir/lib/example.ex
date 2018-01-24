defmodule Example do
  @spec f1(String.t) :: no_return
  defp f1(a) do
    IO.puts(a)
    raise "aa"
  end

  def main() do
    try do
      f1("a")
    rescue
      e -> IO.puts("neko")
    end
  end
end
