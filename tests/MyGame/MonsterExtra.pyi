from __future__ import annotations

import flatbuffers
import numpy as np

import typing

uoffset: typing.TypeAlias = flatbuffers.number_types.UOffsetTFlags.py_type

class MonsterExtra(object):
  @classmethod
  def GetRootAs(cls, buf: bytes, offset: int) -> MonsterExtra: ...
  @classmethod
  def GetRootAsMonsterExtra(cls, buf: bytes, offset: int) -> MonsterExtra: ...
  @classmethod
  def MonsterExtraBufferHasIdentifier(cls, buf: bytes, offset: int, size_prefixed: bool) -> bool: ...
  def Init(self, buf: bytes, pos: int) -> None: ...
  def D0(self) -> float: ...
  def D1(self) -> float: ...
  def D2(self) -> float: ...
  def D3(self) -> float: ...
  def F0(self) -> float: ...
  def F1(self) -> float: ...
  def F2(self) -> float: ...
  def F3(self) -> float: ...
  def Dvec(self, i: int) -> typing.List[float]: ...
  def DvecAsNumpy(self) -> np.ndarray: ...
  def DvecLength(self) -> int: ...
  def DvecIsNone(self) -> bool: ...
  def Fvec(self, i: int) -> typing.List[float]: ...
  def FvecAsNumpy(self) -> np.ndarray: ...
  def FvecLength(self) -> int: ...
  def FvecIsNone(self) -> bool: ...
class MonsterExtraT(object):
  d0: float
  d1: float
  d2: float
  d3: float
  f0: float
  f1: float
  f2: float
  f3: float
  dvec: typing.List[float]
  fvec: typing.List[float]
  def __init__(
    self,
    d0: float = ...,
    d1: float = ...,
    d2: float = ...,
    d3: float = ...,
    f0: float = ...,
    f1: float = ...,
    f2: float = ...,
    f3: float = ...,
    dvec: typing.List[float] | None = ...,
    fvec: typing.List[float] | None = ...,
  ) -> None: ...
  @classmethod
  def InitFromBuf(cls, buf: bytes, pos: int) -> MonsterExtraT: ...
  @classmethod
  def InitFromPackedBuf(cls, buf: bytes, pos: int = 0) -> MonsterExtraT: ...
  @classmethod
  def InitFromObj(cls, monsterExtra: MonsterExtra) -> MonsterExtraT: ...
  def _UnPack(self, monsterExtra: MonsterExtra) -> None: ...
  def Pack(self, builder: flatbuffers.Builder) -> None: ...
  def __eq__(self, other: MonsterExtraT) -> bool: ...
def MonsterExtraStart(builder: flatbuffers.Builder) -> None: ...
def Start(builder: flatbuffers.Builder) -> None: ...
def MonsterExtraAddD0(builder: flatbuffers.Builder, d0: float) -> None: ...
def MonsterExtraAddD1(builder: flatbuffers.Builder, d1: float) -> None: ...
def MonsterExtraAddD2(builder: flatbuffers.Builder, d2: float) -> None: ...
def MonsterExtraAddD3(builder: flatbuffers.Builder, d3: float) -> None: ...
def MonsterExtraAddF0(builder: flatbuffers.Builder, f0: float) -> None: ...
def MonsterExtraAddF1(builder: flatbuffers.Builder, f1: float) -> None: ...
def MonsterExtraAddF2(builder: flatbuffers.Builder, f2: float) -> None: ...
def MonsterExtraAddF3(builder: flatbuffers.Builder, f3: float) -> None: ...
def MonsterExtraAddDvec(builder: flatbuffers.Builder, dvec: uoffset) -> None: ...
def MonsterExtraStartDvecVector(builder: flatbuffers.Builder, num_elems: int) -> uoffset: ...
def StartDvecVector(builder: flatbuffers.Builder, num_elems: int) -> uoffset: ...
def MonsterExtraAddFvec(builder: flatbuffers.Builder, fvec: uoffset) -> None: ...
def MonsterExtraStartFvecVector(builder: flatbuffers.Builder, num_elems: int) -> uoffset: ...
def StartFvecVector(builder: flatbuffers.Builder, num_elems: int) -> uoffset: ...
def MonsterExtraEnd(builder: flatbuffers.Builder) -> uoffset: ...
def End(builder: flatbuffers.Builder) -> uoffset: ...

