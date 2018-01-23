defmodule Example do
  defmodule X do
    @type t :: %__MODULE__{name: String.t}
    defstruct [:name]
  end

  defmodule Y do
    @type t :: %__MODULE__{name: String.t}
    defstruct [:name]
  end

  def hello do
    # test2(%X{name: "test"}) # OK
    # test2(%Y{name: "test"}) # エラー
  end

  @spec test2(X.t) :: boolean
  defp test2(a) do
    IO.inspect(a)
    true
  end
end
